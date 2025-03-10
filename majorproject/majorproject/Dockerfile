# Use Python 3.11
FROM python:3.11

# Install system dependencies for Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev tesseract-ocr-eng

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Copy requirements.txt separately to ensure proper installation
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port for the application
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
