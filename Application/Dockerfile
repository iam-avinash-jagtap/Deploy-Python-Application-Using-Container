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