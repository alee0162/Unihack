import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import json
from flask import Flask, jsonify, request, send_from_directory, render_template
import flask
from werkzeug.utils import secure_filename

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def analyse_image(image_to_analyse):
    text = pytesseract.image_to_string(image_to_analyse)

    details = text.split("\n")
    detailsS = []
    cents = 0
    description = ""
    date = ""
    for i in range(len(details)):
        detailsS = detailsS + details[i].split(" ")
    for i in range(len(detailsS)):
        if detailsS[i].find("$") != -1:
            cents = int(float(detailsS[i][1:])*100)
        elif detailsS[i].find("Description") != -1:
            j=1
            while True:
                if detailsS[i+j] != "":
                    description = description + detailsS[i+j] + " "
                else:
                    break
                j+=1
        elif detailsS[i].find("Paid") != -1:
            if detailsS[i+1] == "on":
                for k in range(3,0,-1):
                    try:
                        date = date + str(int(detailsS[i+1+k]))
                        if k == 3:
                            date = date + "-"
                    except:
                        if k == 2:
                            match detailsS[i+1+k]:
                                case "Jan":
                                    date = date + "01-"
                                    continue
                                case "Feb":
                                    date = date + "02-"
                                    continue
                                case "Mar":
                                    date = date + "03-"
                                    continue
                                case "Apr":
                                    date = date + "04-"
                                    continue
                                case "May":
                                    date = date + "05-"
                                    continue
                                case "Jun":
                                    date = date + "06-"
                                    continue
                                case "Jul":
                                    date = date + "07-"
                                    continue
                                case "Aug":
                                    date = date + "08-"
                                    continue
                                case "Sep":
                                    date = date + "09-"
                                    continue
                                case "Oct":
                                    date = date + "10-"
                                    continue
                                case "Nov":
                                    date = date + "11-"
                                    continue
                                case "Dec":
                                    date = date + "12-"
                                    continue
                                case _:
                                    date = date + "01-"
                                    continue
    return [date, description, cents]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        information = analyse_image(file)
        with open("data.json", "r") as f:
            data = json.load(f)
            data.append({
                    "date": information[1],
                    "description": information[2],
                    "cost": information[3]
            })

            return jsonify(data)

        return jsonify({'message': 'Data stored from', 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == "__main__":
    app.run(debug = True)
"""
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



# Load an image
img = Image.open('images/image3.jpg')

# Perform OCR
text = pytesseract.image_to_string(img)
print(text)

details = text.split("\n")
detailsS = []
cents = 0
description = ""
date = ""
for i in range(len(details)):
    detailsS = detailsS + details[i].split(" ")
for i in range(len(detailsS)):
    if detailsS[i].find("$") != -1:
        cents = int(float(detailsS[i][1:])*100)
    elif detailsS[i].find("Description") != -1:
        j=1
        while True:
            if detailsS[i+j] != "":
                description = description + detailsS[i+j] + " "
            else:
                break
            j+=1
    elif detailsS[i].find("Paid") != -1:
        if detailsS[i+1] == "on":
            for k in range(3,0,-1):
                try:
                    date = date + str(int(detailsS[i+1+k]))
                    if k == 3:
                        date = date + "-"
                except:
                    if k == 2:
                        match detailsS[i+1+k]:
                            case "Jan":
                                date = date + "01-"
                                continue
                            case "Feb":
                                date = date + "02-"
                                continue
                            case "Mar":
                                date = date + "03-"
                                continue
                            case "Apr":
                                date = date + "04-"
                                continue
                            case "May":
                                date = date + "05-"
                                continue
                            case "Jun":
                                date = date + "06-"
                                continue
                            case "Jul":
                                date = date + "07-"
                                continue
                            case "Aug":
                                date = date + "08-"
                                continue
                            case "Sep":
                                date = date + "09-"
                                continue
                            case "Oct":
                                date = date + "10-"
                                continue
                            case "Nov":
                                date = date + "11-"
                                continue
                            case "Dec":
                                date = date + "12-"
                                continue
                            case _:
                                date = date + "01-"
                                continue
"""
"""
# Example API endpoint to process data (e.g., add numbers)
@app.route('/api/analyse', methods=['POST'])
def add_numbers():
    data = request.get_json()  # Get JSON data from the request
    image = data.get('image')
    if image is None:
        return jsonify({"error": "Missing numbers"}), 400
    # Load an image
    img = Image.open('images/image1.jpg')

    # Perform OCR
    text = pytesseract.image_to_string(img)
    print(text)

    details = text.split("\n")

    app = Flask(__name__)
    return jsonify({'Amount': amount, 'Description': description, 'Date': date, 'Flow': flow})

if __name__ == '__main__':
    app.run(debug=True)
"""
"""
# Example API endpoint to get user data
@app.route('/api/user', methods=['GET'])
def get_user():
    user_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    return jsonify(user_data)
"""
"""
# Create a sample plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Sample Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Save the plot to a file
plt.savefig('plot.png')  # Saves the plot as an image file
plt.close()"
"""