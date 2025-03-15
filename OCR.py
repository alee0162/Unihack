import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(__name__)

# Load an image
img = Image.open('images/image1.jpg')

# Perform OCR
text = pytesseract.image_to_string(img)
print(text)

details = text.split("\n")
detailsS = []
cents = 0
description = ""
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
    elif detailsS[i].find("2025") != -1:
        j=1
        while True:
            if detailsS[i+j] != "":
                description = description + detailsS[i+j] + " "
            else:
                break
            j+=1
print(detailsS)
print(description)
print(cents)

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