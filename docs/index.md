# Adventureworks web application

This application is built with the following stack:

- UI: React.js, Typescript
- Backend: Python FastAPI, Redis, Celery, Pydantic
- Infra: Docker, Kubernetes (KIND cluster)
- CI: GitHub Actions
- Docs: MKDocs


## Functionality

### Backend: 


Employee
- CRUD Employee

CRUD PRODUCT
Fetch product category joined with product
Fetch product model, product review, product sub category
Products in the inventory within a timeline
CRUD product review
Add query parameters
Add path parameters
Handle errors
Use nested models
Use cookies
Use middleware
Use asynchronous request to compute statistics with Celery, Redis and Flower
Make 2 microservices talk to each other

Sales
- CRUD store
- Compute sales in a time range
- Compute sales for a store

Purchases
- CRUD Purchases
- CRUD Vendor

### Frontend
- CRUD with error handling for
    - Employee
    - Products
    - Sales
    - Purchases
    - Summary statistics
- Unit testing with Jest

### Infrastructure
- CI/CD pipeline with GitHub Actions for code quality, unit and integration tests and pushing Docker images to container registry
- Package frontend, backend and DB with Docker
- Deploy FE, BE and DB to Kubernetes
- Terraform scripts for setting up AWS VPC, EC2, RDS, ECR, Kubernetes cluster


