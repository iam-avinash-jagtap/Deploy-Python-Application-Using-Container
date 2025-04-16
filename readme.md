# Deploy Python Application Using Container
Hello, in this project you are going to shows how to create and deploy a Python Flask web app using Docker. The app is containerized with a Dockerfile, run on an AWS EC2 instance, and then pushed to Docker Hub. This makes it easy to share, pull, and run the app anywhere with consistency ,future scalability and reuse.
## Pre-requisites
- python application.
- EC2 Instance launched. 
- Linux Basic Knowledge.
- Basic Docker commands knowledge.
- Port 5000 open in EC2 Security Group.
- Docker installed on your EC2 instance.
- Docker Hub account created and accessible.
- Flask application with app.py and Dockerfile.
- VS Code or any editor to write and manage project files.
- Stable Internet connection (for installing packages and pushing/pulling images).
## Learing Objectives
- Understand how to build and run a Python Flask web application.
- Learn how to create and write a Dockerfile to containerize an app.
- Gain hands-on experience in building Docker images and running containers.
- Deploy a Containerized app on an AWS EC2 instance.
- Use Docker commands to manage images and containers.
- Learn how to push and pull Docker images using Docker Hub.
- Understand the importance of port mapping and security groups in deployment.
- Build a reusable, portable, and scalable application environment.

To Create Instacne[,Here](https://github.com/iam-avinash-jagtap/Linux-Server-Deployment-on-AWS-E2)

# Step 1:- Install Docker on EC2 Instance
_To perform all Docker operations, you must first install Docker and switch to the root user to gain full control over your server._
```bash
sudo su -
yum update -y
yum install -y docker
```
Verify Docker is installed:
```bash
docker --version
```

---

# Step 2:- Start Docker Service
_Docker has been successfully installed. Start the Docker service and check if it's running._
```bash
systemctl start docker
systemctl enable docker
systemctl status docker
```

---

# Step 3:- Select Application - Python
_Docker setup is complete. Proceed by choosing your Python application._
_Note:- Pull Application from Github_
```bash
git clone https://github.com/iam-avinash-jagtap/Python-app.git
```
- The application selected is a **Python-app** web application.
- Ensure your application is in a folder with `app.py` is ready.

---

# Step 4:- Create Dockerfile (Using VS Code)
_Your application is ready. Now, write a Dockerfile to build the image._
1. Create a folder on your local machine.
2. Open Vs code in folder
3. Inside it create Dockerfile:
```dockerfile
#Import Base image for application
FROM python:3.9-slim
#Specify project directory
WORKDIR /app
#Copy Code from local to container
COPY . .
#Install Flask to run python application
RUN pip install flask
#Expose port 5000 to run python application
EXPOSE 5000
#Run the application 
CMD ["python", "app.py"]
```
4. Copy Dockerfile on the EC2 instance using `scp`:
```bash
scp -i key.pem -r ./project-folder ec2-user@<EC2-PUBLIC-IP>:/home/ec2-user/python-app
```
#### Your `app.py` and `Dockerfile` are ready to build the Docker image.
---

# Step 5:- Build Docker Image from Dockerfile
_After completing the Dockerfile, you are ready to create a custom image for your application._
```bash
cd python-app
docker build -t python-app .
```
Verify image
```bash
docker images
```

#### The Docker image `python-app` was successfully created.
---

# Step 6:- Create Container from Image
_Once the image is created, you can run a container from your custom image._
```bash
docker images
docker run -d -p 5000:5000 --name python-app python-app
```
Verify your container is up and running
```bash
docker ps
```
---

# Step 7:- Deploy Application in Container
_The container is running. Now, verify the deployment of your application._
- The `python-app` will now be live at `http://<EC2-PUBLIC-IP>:5000`
- Ensure port 5000 is open in the EC2 Security Group.
  
  ![Tech-aj-Home](https://github.com/iam-avinash-jagtap/Deploy-Python-Application-Using-Container/blob/master/Images/Tech-aj-Home.png)


---

# Step 8:- Create Image from Running Container
_Deployment is complete. Now, create an image from your running container to push to Docker Hub._
```bash
docker stop python-app
docker commit  pytho-app avi004/python-app
```
Verify image
```bash
docker images
```
#### A custom Docker image has been generated from your running container.
---

# Step 9:- Create Repository on Docker Hub
_Create a repository on Docker Hub to publicly push your image._
1. Open Browser
2. Go to [https://hub.docker.com](https://hub.docker.com)
3. Log in and click on **Repositories** > **Create Repository**
4. Name the repository `python-app`
_Note:- Image name and Docker hub repository name should be same._

---

# Step 10:- Push Image to Docker Hub
_The setup is almost complete. Now, you can push your image to Docker Hub._
1. Back to termial :
2. Login to Docker Hub:
```bash
docker login
```
_Enter you Docker hub Credintials to login._
3. Push the image:
```bash
docker push avi004/python-app
```
---

![Redpository](https://github.com/iam-avinash-jagtap/Deploy-Python-Application-Using-Container/blob/master/Images/Screenshot%202025-04-16%20122307.png)



#### Your Docker image is now hosted on Docker Hub and can be pulled publicly.
---

# Step 11:- Delete Image from Local Machine
_Your image is now publicly available. You can safely remove it from your Docker server._
```bash
docker rm python-app
docker rmi python-app
docker rmi avi004/python-app
```
#### Your Docker environment is now clean — no images or containers are currently available.
---

# Step 12:- Pull Image from Docker Hub
_Test your setup and verify global access by pulling the image from Docker Hub._
```bash
docker pull avi004/python-app:latest
```
Verify image
```bash
docker images
```
#### You have successfully tested and verified your setup
---  

# Step 13:- Create Container from Pulled Image
_Create a container from the image to check for any environment errors._
```bash

docker run -d -p 5000:5000 --name new-python-app python-app
```
#### Your contianer in running state go to browser and refresh.
---

# Summary 
This project demonstrates how to deploy a Python Flask web application using Docker. The app is containerized using a Dockerfile, built into a lightweight Docker image, and deployed on an AWS EC2 instance. After running the container, the image is pushed to Docker Hub for easy access and versioning. This process ensures that the application can be consistently and portably deployed on any server, making it scalable and adaptable across multiple platforms.

