# Implementation Guide

### Step 1: PII Detection and Masking
```python
import re
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class PIIPattern:
    name: str
    pattern: str
    replacement: str

PII_PATTERNS = [
    PIIPattern("email", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL]"),
    PIIPattern("phone", r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", "[PHONE]"),
    PIIPattern("ssn", r"\b\d{3}-\d{2}-\d{4}\b", "[SSN]"),
    PIIPattern("credit_card", r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b", "[CREDIT_CARD]"),
    PIIPattern("ip_address", r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "[IP_ADDRESS]"),
    PIIPattern("date_of_birth", r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", "[DOB]"),
]

class PIIDetector:
    """Detect and mask PII in text."""

    def __init__(self, patterns: List[PIIPattern] = None):
        self.patterns = patterns or PII_PATTERNS

    def detect(self, text: str) -> List[Tuple[str, str, int, int]]:
        """Detect PII in text. Returns list of (type, value, start, end)."""
        findings = []
        for pattern in self.patterns:
            for match in re.finditer(pattern.pattern, text, re.IGNORECASE):
                findings.append((
                    pattern.name,
                    match.group(),
                    match.start(),
                    match.end()
                ))
        return findings

    def mask(self, text: str) -> str:
        """Mask all PII in text."""
        masked = text
        for pattern in self.patterns:
            masked = re.sub(pattern.pattern, pattern.replacement, masked, flags=re.IGNORECASE)
        return masked

    def redact(self, text: str) -> Tuple[str, dict]:
        """Redact PII and return mapping for restoration."""
        redactions = {}
        counter = {}

        def replace(match, pattern_name, replacement):
            count = counter.get(pattern_name, 0)
            counter[pattern_name] = count + 1
            key = f"{replacement[1:-1]}_{count}"
            redactions[key] = match.group()
            return f"[{key}]"

        result = text
        for pattern in self.patterns:
            result = re.sub(
                pattern.pattern,
                lambda m, p=pattern: replace(m, p.name, p.replacement),
                result,
                flags=re.IGNORECASE
            )

        return result, redactions

# Usage
detector = PIIDetector()
text = "Contact john@example.com or call 555-123-4567"
masked = detector.mask(text)
# "Contact [EMAIL] or call [PHONE]"
```

### Step 2: Pre-processing Pipeline
```python
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

def create_privacy_pipeline(chain):
    """Wrap chain with PII protection."""
    detector = PIIDetector()

    def preprocess(input_data: dict) -> dict:
        """Mask PII before sending to LLM."""
        if "input" in input_data:
            masked, redactions = detector.redact(input_data["input"])
            return {
                **input_data,
                "input": masked,
                "_redactions": redactions
            }
        return input_data

    def postprocess(output: str, redactions: dict = None) -> str:
        """Restore redacted values in output if needed."""
        # Note: Generally we DON'T restore PII in outputs
        # This is just for cases where it's required
        return output

    privacy_chain = (
        RunnableLambda(preprocess)
        | chain
    )

    return privacy_chain

# Usage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Summarize: {input}")
chain = prompt | llm

safe_chain = create_privacy_pipeline(chain)
result = safe_chain.invoke({"input": "User john@example.com reported an issue"})
# LLM sees: "User [EMAIL_0] reported an issue"
```

### Step 3: Data Retention Policies
```python
from datetime import datetime, timedelta
from typing import Optional
import hashlib

class DataRetentionManager:
    """Manage data retention for LLM interactions."""

    def __init__(self, retention_days: int = 30):
        self.retention_days = retention_days
        self.storage = {}  # Replace with actual storage

    def store_interaction(
        self,
        user_id: str,
        input_text: str,
        output_text: str,
        metadata: dict = None
    ) -> str:
        """Store interaction with retention policy."""
        interaction_id = hashlib.sha256(
            f"{user_id}{datetime.now().isoformat()}{input_text}".encode()
        ).hexdigest()[:16]

        # Mask PII before storage
        detector = PIIDetector()

        self.storage[interaction_id] = {
            "user_id_hash": hashlib.sha256(user_id.encode()).hexdigest(),
            "input_masked": detector.mask(input_text),
            "output_masked": detector.mask(output_text),
            "created_at": datetime.now().isoformat(),
            "expires_at": (datetime.now() + timedelta(days=self.retention_days)).isoformat(),
            "metadata": metadata or {}
        }

        return interaction_id

    def cleanup_expired(self) -> int:
        """Remove expired interactions."""
        now = datetime.now()
        expired = [
            k for k, v in self.storage.items()
            if datetime.fromisoformat(v["expires_at"]) < now
        ]

        for key in expired:
            del self.storage[key]

        return len(expired)

    def delete_user_data(self, user_id: str) -> int:
        """GDPR right to erasure - delete all user data."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()
        to_delete = [
            k for k, v in self.storage.items()
            if v["user_id_hash"] == user_hash
        ]

        for key in to_delete:
            del self.storage[key]

        return len(to_delete)
```

### Step 4: Consent Management
```python
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class ConsentType(str, Enum):
    LLM_PROCESSING = "llm_processing"
    DATA_RETENTION = "data_retention"
    ANALYTICS = "analytics"
    TRAINING = "training"  # For fine-tuning

class UserConsent(BaseModel):
    user_id: str
    consents: dict[ConsentType, bool]
    updated_at: datetime
    ip_address: str = None

class ConsentManager:
    """Manage user consent for data processing."""

    def __init__(self):
        self.consents = {}

    def set_consent(self, user_consent: UserConsent) -> None:
        self.consents[user_consent.user_id] = user_consent

    def check_consent(self, user_id: str, consent_type: ConsentType) -> bool:
        """Check if user has given consent."""
        if user_id not in self.consents:
            return False
        return self.consents[user_id].consents.get(consent_type, False)

    def require_consent(self, consent_type: ConsentType):
        """Decorator to require consent before processing."""
        def decorator(func):
            async def wrapper(user_id: str, *args, **kwargs):
                if not self.check_consent(user_id, consent_type):
                    raise PermissionError(
                        f"User {user_id} has not consented to {consent_type.value}"
                    )
                return await func(user_id, *args, **kwargs)
            return wrapper
        return decorator

# Usage
consent_manager = ConsentManager()

@consent_manager.require_consent(ConsentType.LLM_PROCESSING)
async def process_with_llm(user_id: str, input_text: str):
    return await chain.ainvoke({"input": input_text})
```

### Step 5: Audit Logging
```python
import json
from datetime import datetime
from typing import Any

class AuditLogger:
    """Audit log for data access and processing."""

    def __init__(self, log_file: str = "audit.jsonl"):
        self.log_file = log_file

    def log(
        self,
        action: str,
        user_id: str,
        resource: str,
        details: dict = None,
        outcome: str = "success"
    ) -> None:
        """Log an audit event."""
        event = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "user_id_hash": hashlib.sha256(user_id.encode()).hexdigest(),
            "resource": resource,
            "outcome": outcome,
            "details": details or {}
        }

        with open(self.log_file, "a") as f:
            f.write(json.dumps(event) + "\n")

    def log_llm_call(
        self,
        user_id: str,
        model: str,
        prompt_tokens: int,
        has_pii: bool
    ) -> None:
        """Log LLM API call."""
        self.log(
            action="llm_call",
            user_id=user_id,
            resource=f"model/{model}",
            details={
                "prompt_tokens": prompt_tokens,
                "pii_detected": has_pii
            }
        )

# Callback for automatic audit logging
class AuditCallback(BaseCallbackHandler):
    def __init__(self, audit_logger: AuditLogger, user_id: str):
        self.audit_logger = audit_logger
        self.user_id = user_id

    def on_llm_end(self, response, **kwargs) -> None:
        usage = response.llm_output.get("token_usage", {}) if response.llm_output else {}
        self.audit_logger.log_llm_call(
            user_id=self.user_id,
            model=response.llm_output.get("model_name", "unknown") if response.llm_output else "unknown",
            prompt_tokens=usage.get("prompt_tokens", 0),
            has_pii=False  # Set based on detection
        )
```