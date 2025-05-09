# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8081

# Command to run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8081", "src.app:server"] 