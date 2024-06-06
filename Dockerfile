# Use the official Python 3.10 image from the Docker Hub
FROM python:3.12

# Update the package list and install essential tools
RUN apt-get update && \
    apt-get install -y \
    vim \
    telnet \
    inetutils-ping

# Set the working directory inside the container
WORKDIR /app

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install pip==24.0

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Define the command to run the application
CMD ["uvicorn", "src.app_module:http_server", "--host", "0.0.0.0", "--port", "8000"]