# Deploying the FastAPI server to Minikube

This README provides step-by-step instructions for deploying the FastAPI server to a local Kubernetes cluster using Minikube.

# Prerequisites
Before you begin, ensure that you have the following:

* A working installation of Docker
* A working installation of Minikube
* A working installation of kubectl

# Getting Started
## 1. Clone the repository:
`$ git clone https://github.com/username/repo.git`

## 2. Change into the cloned directory:
`$ cd repo`

## 3. Build the Docker image:
`$ docker build -t myapp:latest .`

## 4. Start Minikube:
`$ minikube start`

## 5. Verify that Minikube is running:
`$ kubectl cluster-info`

## 6. Deploy the application to Minikube:
`$ kubectl apply -f kubernetes/`

## 7. Verify that the application is running:
`$ kubectl get pods`

## 8. Expose the deployment as a NodePort:
`kubectl expose deployment/api-server-deployment --type=NodePort --port=80`

## 9. Get the URL of the service:
`minikube service api-server-deployment --url`
Now you should be able to access the API server by visiting the URL returned by the last command in your web browser.

OR 

## 10. Port-forward the application:
`$ kubectl port-forward service/myapp-service 8000:80`

Open a web browser and navigate to http://localhost:8000 to see the running application.

# Clean Up
When you are finished using the application, you can clean up the resources by deleting the Kubernetes deployment and stopping Minikube:

## 1. Delete the Kubernetes deployment:
`$ kubectl delete -f kubernetes/`

## 2. Stop Minikube:
`$ minikube stop`

# Conclusion
This README provides a simple and straightforward way to deploy the FastAPI server to a local Kubernetes cluster using Minikube. By following these instructions, you can quickly get started with Kubernetes and explore the capabilities of this powerful container orchestration platform.
