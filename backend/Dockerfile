# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .
COPY templates/ ./templates/

# Expose port 8000
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
