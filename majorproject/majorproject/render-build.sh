#!/usr/bin/env bash
echo "Installing system dependencies..."
apt-get update && apt-get install -y tesseract-ocr
echo "Tesseract installed successfully!"
