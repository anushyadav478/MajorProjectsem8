# Use the official Python image as the base
FROM python:3.11

# Install system dependencies, including Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*  # Clean up

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Render uses
EXPOSE 8000

# Start the application
CMD ["gunicorn", "majorproject.majorproject.app:app", "--bind", "0.0.0.0:8000"]
