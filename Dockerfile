# # Use an official Python runtime as a parent image
# FROM python:3.9-slim-buster

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install Flask and any other dependencies you might have
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable for Flask to run in production mode

# # Run app.py when the container launches
# CMD ["flask", "run"]


# Use an official Python runtime as the base image
FROM --platform=linux/amd64 python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

EXPOSE 5000

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production


# Run app.py when the container launches
CMD ["python", "app.py"]