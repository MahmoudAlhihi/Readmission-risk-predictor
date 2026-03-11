# Deployment

## Overview

The model is deployed as a containerized FastAPI service.

Deployment stack:

FastAPI -> Docker -> AWS

## Local Run

Run the API locally:

```bash
uvicorn api.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Docker

Build container:

```bash
docker build -t readmission-api .
```

Run container:

```bash
docker run -p 8000:8000 readmission-api
```
## Planned AWS Deployment

Steps:

1. Launch AWS EC2 instance
2. Install Docker
3. Clone the repository
4. Build the Docker image
5. Run the container on port 8000
6. Allow port 8000 in the EC2 security group

The API will then be accessible via:

```text
http://<ec2-ip>:8000/docs
```
