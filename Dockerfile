# Use an official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose Flask default port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
