import pytesseract
from PIL import Image

# Load an image
img = Image.open('images/image1.png')

# Perform OCR
text = pytesseract.image_to_string(img)
print(text)