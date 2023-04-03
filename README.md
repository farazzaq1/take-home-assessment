# take-home-assessment

This is a FastAPI server that exposes two APIs - jumble and audit. The jumble API takes a word and returns a jumbled version of it. The audit API returns the last 10 requests made to the jumble API.

# Prerequisites
Docker
Docker Compose (optional)
Python 3.8+
pipenv (optional)

# Installation
## 1. Clone the repository

git clone https://github.com/your-username/fastapi-server.git

## 2. Install the dependencies

pip install -r requirements.txt

or

pipenv install
(if you prefer to use Pipenv.)


## 3. Start the server

uvicorn api.main:app --host 0.0.0.0 --port 8000
This will start the server on localhost:8000.

# Building the Docker image

## 1. Build the Docker image

docker build -t fastapi-server .
This will build a Docker image with the tag fastapi-server.

## 2. Run the Docker container

docker run -p 8000:8000 fastapi-server
This will start the Docker container and expose port 8000.


# API documentation
You can access the API documentation by going to localhost:8000/docs in your web browser. This will open the Swagger UI, which provides an interactive interface for exploring the APIs.

Testing the APIs
You can test the APIs using curl.

Jumble API

bash
Copy code
curl -X GET http://localhost:8000/jumble/python
This will return a jumbled version of the word python.

Audit API

bash
Copy code
curl -X GET http://localhost:8000/audit
This will return the last 10 requests made to the jumble API.

That's it! You should now be able to update and build the FastAPI server locally.
