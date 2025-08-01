# Use official Python 3.12 slim image as base
FROM python:3.12-slim

# Install distutils and other dependencies needed for building packages
RUN apt-get update && apt-get install -y python3-distutils gcc

# Set working directory inside the container
WORKDIR /app

# Copy all your project files into the container
COPY . /app

# Create a Python virtual environment and install dependencies
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Run your main Python file when the container starts (change bot.py if your main file is different)
CMD ["/opt/venv/bin/python", "bot.py"]
