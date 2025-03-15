from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, render_template
import os
import pytesseract
from PIL import Image
import mysql.connector
import logging

app = Flask(__name__)

# ✅ Setup paths and allowed file types
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ✅ Set the correct path for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if os.path.exists(TESSERACT_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
else:
    raise FileNotFoundError("❌ Tesseract is not installed or the path is incorrect.")

# ✅ Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Helper function to validate uploaded files
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# ✅ Serve the home page
@app.route('/')
def home():
    try:
        return render_template('home.html')  # Ensure home.html exists in the templates folder
    except Exception as e:
        logging.error(f"Error serving home page: {e}")
        return "Error: Unable to load the home page.", 500

# ✅ Serve the index page
@app.route('/index')
def index():
    return render_template('index.html')

# ✅ Handle image upload and processing
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    
    if not file.filename:
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # ✅ Extract text using Tesseract OCR
            extracted_text = pytesseract.image_to_string(Image.open(filepath)).strip()
            cleaned_text = extracted_text.replace("\n", " ").lower()

            if not cleaned_text:
                return jsonify({"error": "No text found in the image"}), 400

            # ✅ Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Yadav@123",  # Replace with YOUR local password
                database="ingredient_db"  # Replace with YOUR local database name
            )
            cursor = conn.cursor()

            # ✅ Process extracted ingredients
            ingredients = [item.strip() for item in cleaned_text.split(",")]

            query = """
                SELECT `Ingredient Name`, `Chemical Name`, `Is Harmful`, `Description`, 
                       `Affected Body Parts`, `Percentage Effect`, `Food Sources` 
                FROM ingredientdatabase 
                WHERE `Ingredient Name` LIKE %s
            """

            results = []
            for ingredient in ingredients:
                cursor.execute(query, (f"%{ingredient}%",))
                results.extend(cursor.fetchall())

            # ✅ Close database connection
            cursor.close()
            conn.close()

            return render_template("result.html", extracted_text=extracted_text, results=results)

        except mysql.connector.Error as db_err:
            logging.error(f"Database error: {db_err}")
            return jsonify({"error": "Database connection error. Check your MySQL settings."}), 500

        except Exception as e:
            logging.error(f"Error during processing: {e}")
            return jsonify({"error": "An error occurred while processing your request."}), 500

    return jsonify({"error": "Invalid file format"}), 400

# ✅ Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
