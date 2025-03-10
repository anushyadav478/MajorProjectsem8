# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# import os
# import pytesseract
# from PIL import Image
# import mysql.connector
# import logging

# app = Flask(__name__)

# # Setup paths and allowed file types
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # Set the correct path for Tesseract (ensure it's installed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Logging setup
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Helper function to validate uploaded files
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # Serve the index page
# @app.route('/')
# def index():
#     try:
#         return send_from_directory('.', 'index.html')
#     except Exception as e:
#         logging.error(f"Error serving index page: {e}")
#         return "Error: Unable to load the index page.", 500

# # Handle image upload and processing
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         try:
#             # Extract text using Tesseract OCR
#             extracted_text = pytesseract.image_to_string(Image.open(filepath)).strip()

#             # Clean and normalize the extracted text
#             cleaned_text = extracted_text.replace("\n", " ").lower()

#             if not cleaned_text:
#                 return jsonify({"error": "No text found in the image"}), 400

#             # Connect to MySQL
#             conn = mysql.connector.connect(
#                 host="localhost",
#                 user="root",  # Replace with your MySQL username
#                 password="Yadav@123",  # Replace with your MySQL password
#                 database="mydatabase"  # Replace with your MySQL database name
#             )
#             cursor = conn.cursor()

#             # Perform database query for each word (split by common delimiters)
#             ingredients = [item.strip() for item in cleaned_text.split(",")]
#             query = "SELECT * FROM project_table WHERE `Ingredient Name` LIKE %s"

#             results = []
#             for ingredient in ingredients:
#                 cursor.execute(query, (f"%{ingredient}%",))
#                 results.extend(cursor.fetchall())

#             # Close the database connection
#             cursor.close()
#             conn.close()

#             # Format and return results
#             result_html = f"<h3>Extracted Text:</h3><p>{extracted_text}</p><br>"

#             if results:
#                 result_html += "<h3>Ingredient Analysis Results:</h3><ul>"
#                 for row in results:
#                     result_html += f"""
#                         <li>
#                             <strong>Ingredient Name:</strong> {row[1]}<br>
#                             <strong>Effect:</strong> {row[2]}<br>
#                             <strong>Affected Body Part:</strong> {row[3]}<br>
#                             <strong>Additional Info:</strong> {row[4]}<br>
#                         </li>
#                         <br>
#                     """
#                 result_html += "</ul>"
#                 return result_html, 200
#             else:
#                 result_html += "<p><strong>No matching ingredients found.</strong></p>"
#                 return result_html, 200

#         except Exception as e:
#             logging.error(f"Error during processing: {e}")
#             return jsonify({"error": f"An error occurred while processing your request: {e}"}), 500
#     else:
#         return jsonify({"error": "Invalid file format"}), 400


# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)


#  # main code statrt idhar se hota hai bhai samjho
# from flask import Flask, request, jsonify, render_template
# from werkzeug.utils import secure_filename
# import os
# import pytesseract
# from PIL import Image
# import mysql.connector
# import logging

# app = Flask(__name__)

# # Setup paths and allowed file types
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # Set the correct path for Tesseract (ensure it's installed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Logging setup
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Helper function to validate uploaded files
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # Serve the index page
# @app.route('/')
# def home():
#     try:
#         return render_template('home.html')  # Ensure home.html exists in the templates folder
#     except Exception as e:
#         logging.error(f"Error serving index page: {e}")
#         return "Error: Unable to load the index page.", 500
# @app.route('/index')
# def index():
#     return render_template('index.html')

# # Handle image upload and processing
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         try:
#             # Extract text using Tesseract OCR
#             extracted_text = pytesseract.image_to_string(Image.open(filepath)).strip()

#             # Clean and normalize the extracted text
#             cleaned_text = extracted_text.replace("\n", " ").lower()

#             if not cleaned_text:
#                 return jsonify({"error": "No text found in the image"}), 400

#             # Connect to MySQL (Railway.app)
#             # conn = mysql.connector.connect(
#             #     host="roundhouse.proxy.rlwy.net",
#             #     port=56076,
#             #     user="root",
#             #     password="GztjLsKIBwpNZuyIxVUfMXTXlbBxQcYn",
#             #     database="railway"
#             # )
#             conn = mysql.connector.connect(
#                   host="localhost",
#                   user="root",  # Replace with your MySQL username
#                   password="Yadav@123",  # Replace with your MySQL password
#                   database="ingredient_db"  # Replace with your MySQL database name
#               )
#             cursor = conn.cursor()

#             # Perform database query for each word (split by common delimiters)
#             ingredients = [item.strip() for item in cleaned_text.split(",")]
#             query = """
#                 SELECT `Ingredient Name`, `Chemical Name`, `Is Harmful`, `Description`, 
#                        `Affected Body Parts`, `Percentage Effect`, `Food Sources` 
#                 FROM  ingredientdatabase 
#                 WHERE `Ingredient Name` LIKE %s
#             """

#             results = []
#             for ingredient in ingredients:
#                 cursor.execute(query, (f"%{ingredient}%",))
#                 results.extend(cursor.fetchall())

#             # Close the database connection
#             cursor.close()
#             conn.close()

#             # Format and return results
#             result_html = f"<h3>Extracted Text:</h3><p>{extracted_text}</p><br>"

#             if results:
#                 result_html += """
#                     <h3>Ingredient Analysis Results:</h3>
#                     <table border="1" style="width:100%; border-collapse: collapse; text-align: left;">
#                         <tr>
#                             <th>Ingredient Name</th>
#                             <th>Chemical Name</th>
#                             <th>Is Harmful</th>
#                             <th>Description</th>
#                             <th>Affected Body Parts</th>
#                             <th>Percentage Effect</th>
#                             <th>Food Sources</th>
#                         </tr>
#                 """
#                 for row in results:
#                     result_html += f"""
#                         <tr>
#                             <td>{row[0]}</td>
#                             <td>{row[1]}</td>
#                             <td>{row[2]}</td>
#                             <td>{row[3]}</td>
#                             <td>{row[4]}</td>
#                             <td>{row[5]}</td>
#                             <td>{row[6]}</td>
#                         </tr>
#                     """
#                 result_html += "</table>"
#             else:
#                 result_html += "<p><strong>No matching ingredients found.</strong></p>"

#             return result_html, 200

#         except Exception as e:
#             logging.error(f"Error during processing: {e}")
#             return jsonify({"error": f"An error occurred while processing your request: {e}"}), 500
#     else:
#         return jsonify({"error": "Invalid file format"}), 400


# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)




# Third code
# import os
# import mysql.connector
# from flask import Flask, request, jsonify  # Make sure you have Flask installed: pip install Flask
# from PIL import Image  # Make sure you have Pillow installed: pip install Pillow
# import pytesseract  # Make sure you have pytesseract installed: pip install pytesseract

# app = Flask(__name__)

# # Set the path to your Tesseract executable (if needed)
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Example Windows path

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image part"}), 400
#     image = request.files['image']
#     if image.filename == '':
#         return jsonify({"error": "No selected image"}), 400

#     try:
#         # 1. Save the image temporarily
#         filepath = "uploads/" + image.filename  # Create 'uploads' folder if it doesn't exist
#         image.save(filepath)

#         # 2. Extract text using Tesseract OCR
#         extracted_text = pytesseract.image_to_string(Image.open(filepath)).strip()

#         # 3. Clean and normalize the extracted text
#         cleaned_text = extracted_text.replace("\n", " ").lower()  # Replace newlines with spaces

#         if not cleaned_text:
#             return jsonify({"error": "No text found in the image"}), 400

#         # 4. Connect to MySQL database
#         try:
#             if os.environ.get("VERCEL"):  # Check if running on Vercel
#                 mydb = mysql.connector.connect(
#                     host=os.environ.get("MYSQLHOST"),
#                     port=os.environ.get("MYSQLPORT"),
#                     user=os.environ.get("MYSQLUSER"),
#                     password=os.environ.get("MYSQLPASSWORD"),
#                     database=os.environ.get("MYSQLDATABASE")
#                 )
#             else:  # Local development
#                 mydb = mysql.connector.connect(
#                     host="localhost",
#                     user="root",
#                     password="Yadav@123",  # Replace with YOUR local password
#                     database="mydatabase"  # Replace with YOUR local database name
#                 )

#             # 5. Insert data into MySQL (example)
#             mycursor = mydb.cursor()
#             sql = "INSERT INTO your_table (extracted_text) VALUES (%s)"  # Replace your_table
#             val = (cleaned_text,)  # Make sure cleaned_text is a tuple
#             mycursor.execute(sql, val)
#             mydb.commit()

#             mydb.close()  # Close the database connection

#         except mysql.connector.Error as mysql_err:
#             print(f"MySQL Error: {mysql_err}")
#             return jsonify({"error": f"Database error: {mysql_err}"}), 500

#         # 6. Remove the temporary image file (optional, but good practice)
#         os.remove(filepath)

#         return jsonify({"message": "Image processed and data stored successfully"}), 200

#     except Exception as e:  # Catch any other potential errors
#         print(f"Error processing image: {e}")  # Print for debugging
#         return jsonify({"error": str(e)}), 500  # Return error to the frontend

# if __name__ == '__main__':
#     app.run(debug=True)  # Set debug=False for production


# final code of styling 


# from werkzeug.utils import secure_filename
# from flask import Flask, request, jsonify, render_template
# from urllib.parse import quote as url_quote
# import os
# import pytesseract
# from PIL import Image
# import mysql.connector
# import logging
# import shutil

# app = Flask(__name__)

# # Setup paths and allowed file types
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # Set the correct path for Tesseract (ensure it's installed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Logging setup
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Helper function to validate uploaded files
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # Serve the index page
# @app.route('/')
# def home():
#     try:
#         return render_template('home.html')  # Ensure home.html exists in the templates folder
#     except Exception as e:
#         logging.error(f"Error serving index page: {e}")
#         return "Error: Unable to load the index page.", 500
# @app.route('/index')
# def index():
#     return render_template('index.html')

# # Handle image upload and processing


# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['image']

#     # Ensure filename is not empty before using secure_filename
#     if not file.filename:
#         return jsonify({"error": "No selected file"}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         try:
#             extracted_text = pytesseract.image_to_string(Image.open(filepath)).strip()
#             cleaned_text = extracted_text.replace("\n", " ").lower()

#             if not cleaned_text:
#                 return jsonify({"error": "No text found in the image"}), 400

#             conn = mysql.connector.connect(
#                 host="shortline.proxy.rlwy.net",
#                 port=59867,
#                 user="root",
#                 password="SaGzejNBHlXVTYLghHCWuaErbkwwCvba",
#                 database="ingredient_db"
#             )
#             cursor = conn.cursor()

#             ingredients = [item.strip() for item in cleaned_text.split(",")]
#             query = """
#                 SELECT `Ingredient Name`, `Chemical Name`, `Is Harmful`, `Description`, 
#                        `Affected Body Parts`, `Percentage Effect`, `Food Sources` 
#                 FROM ingredientdatabase 
#                 WHERE `Ingredient Name` LIKE %s
#             """

#             results = []
#             for ingredient in ingredients:
#                 cursor.execute(query, (f"%{ingredient}%",))
#                 results.extend(cursor.fetchall())

#             cursor.close()
#             conn.close()

#             return render_template("result.html", extracted_text=extracted_text, results=results)

#         except Exception as e:
#             logging.error(f"Error during processing: {e}")
#             return jsonify({"error": f"An error occurred while processing your request: {e}"}), 500

#     return jsonify({"error": "Invalid file format"}), 400




# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)



from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, render_template
from urllib.parse import quote as url_quote
import os
import pytesseract
from PIL import Image
import mysql.connector
import logging
import shutil

app = Flask(__name__)

# ✅ Fix Tesseract path dynamically (works on Windows, Linux, and Render)
if shutil.which("tesseract"):
    pytesseract.pytesseract.tesseract_cmd = shutil.which("tesseract")
else:
    raise FileNotFoundError("❌ Tesseract is not installed. Install it before running the app.")

# Setup paths and allowed file types
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Helper function to validate uploaded files
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Serve the index page
@app.route('/')
def home():
    try:
        return render_template('home.html')  # Ensure home.html exists in the templates folder
    except Exception as e:
        logging.error(f"Error serving index page: {e}")
        return "Error: Unable to load the index page.", 500

@app.route('/index')
def index():
    return render_template('index.html')

# Handle image upload and processing
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
            extracted_text = pytesseract.image_to_string(Image.open(filepath)).strip()
            cleaned_text = extracted_text.replace("\n", " ").lower()

            if not cleaned_text:
                return jsonify({"error": "No text found in the image"}), 400

            conn = mysql.connector.connect(
                host="shortline.proxy.rlwy.net",
                port=59867,
                user="root",
                password="SaGzejNBHlXVTYLghHCWuaErbkwwCvba",
                database="ingredient_db"
            )
            cursor = conn.cursor()

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

            cursor.close()
            conn.close()

            return render_template("result.html", extracted_text=extracted_text, results=results)

        except Exception as e:
            logging.error(f"Error during processing: {e}")
            return jsonify({"error": f"An error occurred while processing your request: {e}"}), 500

    return jsonify({"error": "Invalid file format"}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)


