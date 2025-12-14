# SimpleTimeService - DevOps 

# project overview
- SimpleTimeService is a lightweight web service designed to demonstrate a complete DevOps    workflow using a minimal application.
- The project covers the full lifecycle of an application, from development and containerization to automation and cloud deployment.
- The application runs as a web server and exposes a REST endpoint.
- When the root endpoint (/) is accessed, it returns a JSON response containing:
  - Current timestamp
  - IP address of the client making the request

# what does this project do:
- Runs a simple web service
The application starts a small web server that listens for HTTP requests.
- Provides an API endpoint
When a user accesses the root URL (/) in a browser or using a tool like curl, the application responds with a JSON output.
- Returns useful runtime information
The JSON response includes:
 - The current date and time (timestamp)
 - The IP address of the user making the request
- Supports health checks
A separate /health endpoint is available so that load balancers or monitoring tools can check whether the application is running properly.
- Runs inside a Docker container
The application is packaged inside a Docker container, making it easy to run the same way on any system without worrying about local setup differences.
- Automates the build process
A CI/CD pipeline using GitHub Actions automatically builds the Docker image and pushes it to DockerHub whenever code is pushed to the repository.
- Can be deployed to the cloud
Using Terraform, the application can be deployed on AWS using ECS Fargate and accessed through a public load balancer.


# sample response

json
{
  "timestamp": "2025-01-01T10:30:00Z",
  "ip": "1.2.3.4"
}

## Technology stack

- Programming Language: Python (Flask)
- Containerization: Docker
- Container Registry: DockerHub
- CI/CD: GitHub Actions
- Cloud Provider: AWS
- Infrastructure as Code: Terraform
- Container Orchestration: AWS ECS (Fargate)
- Load Balancer: Application Load Balancer (ALB)

## Repository structure

├── app
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── terraform
│   ├── main.tf
│   ├── providers.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── .gitignore
└── README.md

## step 1 : Running the Application Locally (Docker)

- prerequisites : Docker installed locally

# Build the docker image
cd app
docker build -t simpletimeservice:local .

# Run the Container
docker run -p 8080:8080 simpletimeservice:local

# Test the Application
curl http://localhost:8080/
curl http://localhost:8080/health

## step 2: Docker Image
The application image is published to a public DockerHub repository.
comand -> docker pull simran2310/simple-timeservice:latest

## step 3: CI/CD Pipeline (GitHub Actions)
- Any new code is pushed to the github repository. 
- A CI/CD pipeline is configured using GitHub Actions.
- The pipeline triggers automatically on every push to the main branch
- It will build the Docker image from the app/ directory
- It will push the image to DockerHub
- Secrets and variables in github Action is stored securey using Github Secrets
- no passwords or tokens are hardcoded in the repository

## step 4: Infrastructure Deployment (AWS + Terraform)
Infrastructure is provisioned using Terraform.
- Architecture 
  - VPC with public and private subnets
  - ECS Fargate cluster running the container
  - ECS tasks deployed in private subnets
  - Application Load Balancer deployed in public subnets
  - NAT Gateway used for outbound internet access
- Prerequisites : AWS account, AWS CLI installed and configured and Terraform installed
- configure AWS credentials by using
  command -> aws configure

## Deploy infrastructure
- go to terraform folder -> cd terraform
- initialize terraform -> terraform init
- run the command for plan -> terraform plan -out plan.out
- apply the plan.out -> terraform apply "plan.out"

After deployment, Terraform outputs the ALB DNS name, make sure to copy and paste in notepad.

- Access the application 
run the command -> curl http://<ALB_DNS_NAME>/
(replace <ALB_DNS_NAME> with the ALB_DNS_NAME that you copied)

## step 5: CLEANUP (very important)
cleanup is important to avoid the cloud charges, all AWS resources should be destroyed after verification:
- run the command -> terraform destroy -auto-approve


## Notes
- The container runs as a non-root user
- Terraform local state and provider binaries are intentionally ignored using .gitignore
- No secrets or credentials are committed to the repository
- The project follows DevOps best practices for security, automation, and cost awareness