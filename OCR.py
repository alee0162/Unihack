import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Load an image
img = Image.open('images/image1.jpg')

# Perform OCR
text = pytesseract.image_to_string(img)
print(text)

details = text.split("\n")
print(details)


# Create a sample plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Sample Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Save the plot to a file
plt.savefig('plot.png')  # Saves the plot as an image file
plt.close()