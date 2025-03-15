import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Load an image
img = Image.open('images/image1.jpg')

# Perform OCR
text = pytesseract.image_to_string(img)
print(text)