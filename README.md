# Cloud-Native

Kubernetes Deployment & Service with Flask App

Overview

This project sets up a Flask monitoring application deployed on Kubernetes using Amazon EKS and Amazon ECR. The application monitors system metrics (CPU & Memory usage) and provides alerts when resource utilization is high.

Components

1. Flask Application

Displays real-time CPU and memory usage.

Generates alerts when resource usage exceeds 80%.

2. Docker Setup

Uses a Dockerfile based on Python 3.9 Slim.

Installs necessary dependencies from requirements.txt.

Exposes port 5000 for the Flask app.

3. Amazon ECR

ecr.py automates the creation of an ECR repository.

Stores the Flask application image for Kubernetes deployment.

4. Amazon EKS

eks.py automates the creation and management of an EKS cluster.

Deploys the Flask application to the Kubernetes cluster.

5. Kubernetes Deployment & Service

Defines a Deployment for the Flask app with one replica.

Deploys a Service to expose the application within the cluster.

Setup Instructions

Prerequisites

Ensure you have the following installed:

Docker

AWS CLI

Kubernetes CLI (kubectl)

Python 3.x

1. Set Up AWS EKS & ECR

Run the provided scripts to create the necessary AWS resources:

python3 ecr.py   # Creates the ECR repository
python3 eks.py   # Creates the EKS cluster

2. Build & Push Docker Image

aws ecr create-repository --repository-name my_monitoring_app_image
export ECR_URI=692859913278.dkr.ecr.us-east-1.amazonaws.com/my_monitoring_app_image
docker build -t $ECR_URI .
docker push $ECR_URI

3. Deploy to Kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

4. Access the Flask App

Get the service details:

kubectl get svc my-flask-service

Retrieve the Cluster IP or NodePort and access the app in the browser.

├── app.py                # Flask application for monitoring CPU & memory
├── Dockerfile            # Containerization setup
├── requirements.txt      # Python dependencies
├── ecr.py                # Automates Amazon ECR setup
├── eks.py                # Automates Amazon EKS setup
├── index.html            # Frontend UI
└── README.md             # Documentation
