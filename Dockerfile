# Use the official Python image from the Docker Hub
FROM python:3.8.12

# Install required packages
RUN apt-get update && apt-get install -y curl

# Install Postman CLI
RUN curl -o- "https://dl-cli.pstmn.io/install/linux64.sh" | sh

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages from requirements.txt
RUN pip install -r requirements.txt

# Set the command to be run when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
