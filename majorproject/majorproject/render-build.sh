#!/usr/bin/env bash
echo "Updating package lists..."
apt-get update

echo "Installing Tesseract-OCR..."
apt-get install -y tesseract-ocr

echo "Tesseract installation completed!"
