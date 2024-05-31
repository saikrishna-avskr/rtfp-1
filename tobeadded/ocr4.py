import pytesseract 
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import os
from PIL import Image
file_name="name.png"


text = pytesseract.image_to_string(Image.open(file_name))  
print(text)