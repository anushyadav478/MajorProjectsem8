# Use an official Python runtime as the base image
FROM python:3.11

# Install Tesseract OCR and dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r majorproject/majorproject/requirements.txt

# Expose the port Render uses
EXPOSE $PORT

# Start the application
CMD ["gunicorn", "majorproject.majorproject.app:app", "--bind", "0.0.0.0:8000"]
