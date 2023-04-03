# API-Server Chart 🚀
This Helm chart installs and configures the My API Server on a Kubernetes cluster.

# Prerequisites
Before you can install this chart, you must have the following:

* A running Kubernetes cluster 🏃‍♀️🏃‍♂️
* The kubectl command-line tool installed and configured to communicate with your cluster 🛠️
* The Helm command-line tool installed on your local machine 🧑‍💻

# Installing the Chart 
To install the chart, follow these steps:

## Install the chart using the helm install command:

`helm install my-release my-repo/my-chart`

## This command installs the chart using the release name my-release.

You can customize the installation by providing a values.yaml file with your own configuration values. For example:
`helm install my-release my-repo/my-chart -f values.yaml`

## Verify that the application is running:
`kubectl get pods`


# Uninstalling the Chart
To uninstall the chart, use the helm uninstall command:

helm uninstall my-release
This command removes all of the Kubernetes resources created by the chart.

