FROM python:3.11

# Install required system packages, including Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r majorproject/majorproject/requirements.txt

# Expose the port Render uses
EXPOSE $PORT

# Start the application
CMD ["gunicorn", "majorproject.majorproject:app", "--bind", "0.0.0.0:8000"]
