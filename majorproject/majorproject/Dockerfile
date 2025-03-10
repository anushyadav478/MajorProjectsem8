FROM python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y tesseract-ocr

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install -r majorproject/majorproject/requirements.txt

# Expose the port for the application
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "majorproject.majorproject.app:app", "--bind", "0.0.0.0:5000"]
