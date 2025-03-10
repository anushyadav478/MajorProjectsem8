#!/bin/bash

# Install Tesseract OCR
apt-get update && apt-get install -y tesseract-ocr

# Run Gunicorn to start the app
gunicorn majorproject.majorproject.app:app --bind 0.0.0.0:$PORT
