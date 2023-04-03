# Setting Up Minikube on Ubuntu :sparkles:

These instructions will guide you on how to install Minikube on Ubuntu.

# Prerequisites :books:
* Ubuntu operating system
* sudo privileges
* curl
 
# Step 1: Install kubectl :rocket:

## Download kubectl binary using curl:
`curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl`

## Make the binary executable:
`chmod +x ./kubectl`

## Move the binary to /usr/local/bin to make it available on your system:
`sudo mv ./kubectl /usr/local/bin/kubectl`

# Step 2: Install Docker :bulb:
## Update your system's package list:
`sudo apt-get update -y`

## Install Docker:
`sudo apt-get install -y docker.io`

## Step 3: Install Minikube :books:
## Download Minikube binary using curl:
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

## Switch to root user:
`sudo -i`

## Verify that Docker is installed and running by checking the status of the Docker daemon:
`docker ps`

## Add the current user to the docker group:
`sudo usermod -aG docker $USER && newgrp docker`

## Start Minikube with Docker driver:
`minikube start --driver=docker`

## Check the status of Minikube:
`minikube status`

You have now successfully installed Minikube on Ubuntu. :heavy_check_mark:
