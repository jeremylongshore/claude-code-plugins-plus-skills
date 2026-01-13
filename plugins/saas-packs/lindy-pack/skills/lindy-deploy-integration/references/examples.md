# Examples

### Docker Deployment
```yaml
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY dist ./dist
ENV NODE_ENV=production
CMD ["node", "dist/index.js"]
```

```yaml
# Deploy job
- name: Build and push Docker image
  run: |
    docker build -t my-lindy-app:${{ github.sha }} .
    docker push my-lindy-app:${{ github.sha }}
```