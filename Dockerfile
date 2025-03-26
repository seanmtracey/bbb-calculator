# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install sympy
RUN pip install sympy

# Copy your Python script into the container
COPY main.py .

# Run the script
CMD ["python", "main.py"]
