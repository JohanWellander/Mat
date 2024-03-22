import pytesseract
from PIL import Image
import os


# Open the image file
image = Image.open("g:/Min enhet/G-OneDrive/MPSYS/Projects/Mat/kvitto.png")

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)