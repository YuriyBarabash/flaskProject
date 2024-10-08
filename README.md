# Flask Project

## Overview

This project is a simple Flask application that serves as a REST API. The main functionality is to return a greeting 
message based on the user's input.

### Features

- A `/api/greet` endpoint that accepts a GET request with a query parameter `name` and returns a JSON response with 
a greeting message.

### Example

If you send a GET request to `/api/greet?name=Yuriy`, the API will respond with:

```json
{
  "message": "Hello, Yuriy!"
}
```
## How to Build and Run the Docker Container

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- `Docker`: You can download and install Docker from the official website: https://www.docker.com/get-started

### Steps to Build and Run the Docker Container
  1. Pull the Docker image from Docker Hub:

     Replace your-dockerhub-username with your Docker Hub username and your-image-name with the name of your Docker image

     `docker pull yuriybarabash/flask_project`
  
  2. Run the Docker container:
  
     `docker run -d -p 5000:5000 yuriybarabash/flask_project`  
     `-d: Runs the container in detached mode (in the background).`  
     `-p 5000:5000: Maps port 5000 of your host machine to port 5000 of the container, where the Flask app is running.`
     
## Accessing the Application

Once the container is running, you can access the Flask application by navigating to:
  `http://localhost:5000`

## How to Test the API Endpoint

After the Docker container is up and running, you can test the /api/greet endpoint as follows:
  1. Using a Web Browser or Postman:
     Open your web browser or Postman and navigate to:
      
     http://localhost:5000/api/greet?name=Yuriy
  
  2. Using curl in the Terminal:
     You can also test the endpoint using curl from the command line:
     
     `curl http://localhost:5000/api/greet?name=Yuiy`
  
  This will return:
   
 ```json
{
  "message": "Hello, Yuriy!"
}
```

## Development
### If you want to make changes to the project or run it locally without Docker, follow these steps:
   1. Clone the Repository:  
      `git clone https://github.com/YuriyBarabash/flaskProject.git`    
      `cd flaskProject`
   
   2. Create and Activate a Virtual Environment:
      On Windows:
         
      `python -m venv venv`  
       `venv\Scripts\activate`
      
      On macOS/Linux:
      
      `python3 -m venv venv`  
      `source venv/bin/activate`
      
   3. Install the Dependencies: 
     
      `pip install -r requirements.txt`
      
   4. Run the Flask Application:
   
      `flask run`


   
   
