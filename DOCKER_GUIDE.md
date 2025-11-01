# 🐳 Docker Deployment Guide

Complete guide for running the AptoCom AI Agent in Docker containers.

---

## 📋 Prerequisites

- **Docker** installed ([Get Docker](https://docs.docker.com/get-docker/))
- **Docker Compose** installed (included with Docker Desktop)
- **Google Gemini API Key** (from https://aistudio.google.com/apikey)

---

## 🚀 Quick Start (3 Methods)

### **Method 1: Using Docker Compose (Recommended)**

```bash
# 1. Make sure .env file exists with your API key
# .env should contain:
# GOOGLE_API_KEY=your_actual_api_key_here
# PORT=5000

# 2. Build and start container
docker-compose up -d

# 3. Check if running
docker-compose ps

# 4. View logs
docker-compose logs -f

# 5. Test the API
curl http://localhost:5000/health

# 6. Stop container
docker-compose down
```

### **Method 2: Using Dockerfile Directly**

```bash
# 1. Build the image
docker build -t aptocom-ai-agent:latest .

# 2. Run the container
docker run -d \
  --name aptocom-ai-agent \
  -p 5000:5000 \
  -e GOOGLE_API_KEY=your_actual_api_key_here \
  -e PORT=5000 \
  aptocom-ai-agent:latest

# 3. Check logs
docker logs -f aptocom-ai-agent

# 4. Stop container
docker stop aptocom-ai-agent
docker rm aptocom-ai-agent
```

### **Method 3: Using .env File (Most Secure)**

```bash
# 1. Ensure .env file exists
cat .env

# 2. Build image
docker build -t aptocom-ai-agent:latest .

# 3. Run with env file
docker run -d \
  --name aptocom-ai-agent \
  -p 5000:5000 \
  --env-file .env \
  aptocom-ai-agent:latest

# 4. Test
curl http://localhost:5000/health
```

---

## 🧪 Testing the Container

### Health Check
```bash
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "service": "AptoCom Proposal Agent"
}
```

### Evaluate a Proposal
```bash
curl -X POST http://localhost:5000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Community Dashboard",
    "description": "Build analytics dashboard for community engagement",
    "requested_amount": 25000,
    "team_info": "3 developers with 5 years experience",
    "budget_breakdown": "Development: 15k, Design: 7k, Testing: 3k",
    "milestones": "M1: Design (1 month), M2: Development (2 months)",
    "expected_roi": "Increase engagement by 40%",
    "risk_factors": "Timeline delays, technical complexity"
  }'
```

---

## 📦 Docker Files Explained

### **Dockerfile**
The blueprint for building the container image:
- Based on Python 3.11 slim image
- Installs dependencies from `requirements.txt`
- Copies application code
- Exposes port 5000
- Includes health check
- Runs `api.py` on startup

### **.dockerignore**
Prevents unnecessary files from being copied into the image:
- Virtual environments (`venv/`)
- API keys (`.env`)
- Git files
- IDE settings
- Cache files

### **docker-compose.yml**
Orchestration file for easy deployment:
- Defines service configuration
- Maps ports
- Loads environment variables
- Sets up networking
- Configures health checks and restart policy

---

## 🔧 Common Docker Commands

### Container Management
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Start container
docker start aptocom-ai-agent

# Stop container
docker stop aptocom-ai-agent

# Restart container
docker restart aptocom-ai-agent

# Remove container
docker rm aptocom-ai-agent

# Remove container forcefully
docker rm -f aptocom-ai-agent
```

### Image Management
```bash
# List images
docker images

# Remove image
docker rmi aptocom-ai-agent:latest

# Build with no cache
docker build --no-cache -t aptocom-ai-agent:latest .

# Tag image for registry
docker tag aptocom-ai-agent:latest yourusername/aptocom-ai-agent:v1.0
```

### Logs & Debugging
```bash
# View logs (live)
docker logs -f aptocom-ai-agent

# View last 100 lines
docker logs --tail 100 aptocom-ai-agent

# Execute command in running container
docker exec -it aptocom-ai-agent /bin/bash

# Check container resource usage
docker stats aptocom-ai-agent

# Inspect container details
docker inspect aptocom-ai-agent
```

### Docker Compose Commands
```bash
# Build and start
docker-compose up -d

# Build without cache
docker-compose build --no-cache

# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# View logs
docker-compose logs -f

# Restart services
docker-compose restart

# Scale services
docker-compose up -d --scale aptocom-ai-agent=3
```

---

## 🌐 Deploying to Cloud Platforms

### **Docker Hub**

1. **Build and tag image:**
```bash
docker build -t yourusername/aptocom-ai-agent:v1.0 .
```

2. **Login to Docker Hub:**
```bash
docker login
```

3. **Push image:**
```bash
docker push yourusername/aptocom-ai-agent:v1.0
```

4. **Share with others:**
```bash
# They can pull and run with:
docker pull yourusername/aptocom-ai-agent:v1.0
docker run -d -p 5000:5000 -e GOOGLE_API_KEY=key yourusername/aptocom-ai-agent:v1.0
```

### **AWS ECS (Elastic Container Service)**

```bash
# 1. Tag for ECR
docker tag aptocom-ai-agent:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/aptocom-ai-agent:latest

# 2. Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com

# 3. Push to ECR
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/aptocom-ai-agent:latest

# 4. Deploy via ECS Console or CLI
```

### **Google Cloud Run**

```bash
# 1. Tag for GCR
docker tag aptocom-ai-agent:latest gcr.io/your-project-id/aptocom-ai-agent:latest

# 2. Push to GCR
docker push gcr.io/your-project-id/aptocom-ai-agent:latest

# 3. Deploy to Cloud Run
gcloud run deploy aptocom-ai-agent \
  --image gcr.io/your-project-id/aptocom-ai-agent:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_key
```

### **Azure Container Instances**

```bash
# 1. Build and push to Azure Container Registry
az acr build --registry myregistry --image aptocom-ai-agent:latest .

# 2. Deploy to ACI
az container create \
  --resource-group myResourceGroup \
  --name aptocom-ai-agent \
  --image myregistry.azurecr.io/aptocom-ai-agent:latest \
  --dns-name-label aptocom-ai \
  --ports 5000 \
  --environment-variables GOOGLE_API_KEY=your_key
```

### **Render.com**

1. Create new **Web Service**
2. Connect GitHub repo
3. Select **Docker** as environment
4. Add environment variable: `GOOGLE_API_KEY`
5. Deploy automatically

### **Railway.app**

1. Create new project
2. Deploy from GitHub
3. Railway auto-detects Dockerfile
4. Add `GOOGLE_API_KEY` in variables
5. Deploy

---

## 🔒 Security Best Practices

### 1. **Never Hardcode API Keys**
```bash
# ❌ BAD
docker run -e GOOGLE_API_KEY=AIzaSyB... aptocom-ai-agent

# ✅ GOOD
docker run --env-file .env aptocom-ai-agent
```

### 2. **Use Docker Secrets (Swarm/Kubernetes)**
```yaml
version: '3.8'
services:
  app:
    image: aptocom-ai-agent
    secrets:
      - google_api_key
    environment:
      - GOOGLE_API_KEY_FILE=/run/secrets/google_api_key

secrets:
  google_api_key:
    external: true
```

### 3. **Scan for Vulnerabilities**
```bash
# Install Trivy
docker run aquasec/trivy image aptocom-ai-agent:latest

# Or use Docker Scout
docker scout cves aptocom-ai-agent:latest
```

### 4. **Use Non-Root User**
Add to Dockerfile:
```dockerfile
RUN useradd -m -u 1000 appuser
USER appuser
```

---

## 📊 Monitoring & Logging

### **View Container Stats**
```bash
docker stats aptocom-ai-agent
```

### **Export Logs to File**
```bash
docker logs aptocom-ai-agent > agent.log 2>&1
```

### **Log Rotation**
```bash
docker run -d \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  aptocom-ai-agent:latest
```

---

## 🛠️ Troubleshooting

### **Container Exits Immediately**
```bash
# Check logs
docker logs aptocom-ai-agent

# Run interactively to debug
docker run -it aptocom-ai-agent:latest /bin/bash
```

### **Port Already in Use**
```bash
# Find process using port 5000
netstat -ano | findstr :5000  # Windows
lsof -i :5000                 # macOS/Linux

# Use different port
docker run -p 8080:5000 aptocom-ai-agent:latest
```

### **Environment Variables Not Working**
```bash
# Verify env vars inside container
docker exec aptocom-ai-agent env | grep GOOGLE_API_KEY

# Check if .env file is correct
cat .env
```

### **Image Build Fails**
```bash
# Clean Docker cache
docker system prune -a

# Build with verbose output
docker build --progress=plain -t aptocom-ai-agent:latest .
```

### **Health Check Failing**
```bash
# Check health status
docker inspect --format='{{.State.Health.Status}}' aptocom-ai-agent

# View health check logs
docker inspect --format='{{range .State.Health.Log}}{{.Output}}{{end}}' aptocom-ai-agent
```

---

## 📦 Optimizing Image Size

### **Current Size**
```bash
docker images aptocom-ai-agent:latest
```

### **Multi-Stage Build (Advanced)**
```dockerfile
# Build stage
FROM python:3.11 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "api.py"]
```

---

## 🎯 Production Checklist

- [ ] API key stored securely (not in Dockerfile)
- [ ] `.dockerignore` configured properly
- [ ] Health check implemented
- [ ] Logging configured
- [ ] Resource limits set (memory, CPU)
- [ ] Container scanned for vulnerabilities
- [ ] Non-root user configured
- [ ] Restart policy set
- [ ] Monitoring enabled
- [ ] Backup strategy in place

---

## 📚 Additional Resources

- **Docker Docs:** https://docs.docker.com
- **Docker Hub:** https://hub.docker.com
- **Docker Compose:** https://docs.docker.com/compose
- **Best Practices:** https://docs.docker.com/develop/dev-best-practices

---

## 🤝 Need Help?

If you encounter issues:
1. Check container logs: `docker logs aptocom-ai-agent`
2. Verify environment variables: `docker exec aptocom-ai-agent env`
3. Test health endpoint: `curl http://localhost:5000/health`
4. Review Docker documentation

---

**Your AI agent is now containerized and ready for deployment anywhere! 🐳🚀**
