# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install required dependencies
RUN pip install flask requests

# Expose port 5000 for communication
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]



