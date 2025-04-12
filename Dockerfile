# Use the official Python image as the base image
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Install the required packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY pysubstitutor/ /app
COPY data/ /app/data/

# Set the default command to run the Python application
CMD ["python", "-m", "pysubstitutor"]