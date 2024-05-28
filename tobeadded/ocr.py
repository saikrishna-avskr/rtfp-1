# https://github.com/UB-Mannheim/tesseract/wiki 
# use the above link to get pytesseract

import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _,image = camera.read()
    cv2.imshow('Text detection',image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()

def tesseract():
    #after tesseract installation , put the path here
    # it would end in smtg like \tesseract-ocr\tesseract.exe
    #pathtotess=r""
    Imagepath = 'test1.jpg'
    #pytesseract.tesseract_cmd=pathtotess
    text=pytesseract.image_to_string(Image.open(Imagepath))
    print(text)
    