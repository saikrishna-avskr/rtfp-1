
import cv2
import numpy as np
font_scale=1.5
font = cv2.FONT_HERSHEY_PLAIN
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
cap=cv2.VideoCapture(1)
#cap.set(cv2.CAP_PROP_FPS,170)

if not cap.isOpened():
    cap=cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

cntr=0;
while True:
    ret,frame=cap.read()
    cntr=cntr+1;

    if((cntr%20)==0):

        imgH,imgW,_=frame.shape
        #eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        x1,y1,w1,h1=0,0,imgH,imgW
        imgchar=pytesseract.image_to_string(frame)
        imgboxes=pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes=boxes.split(' ')
            x,y,w,h=int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
            cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
        cv2.putText(frame,imgchar,(x1+int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_SIMPLEX,0.7, (0,0,255),2)

        font=cv2.FONT_HERSHEY_SIMPLEX

        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #print(faceCascade.empty())
        #faces = faceCascade.detectMultiScale(gray,1.1,4)

        #Draw a rect around the faces 
        #for(x,y,w,h) in faces:
        #    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #use putTest() method for inserting text on video

        cv2.imshow('Text Detection Tutorial',frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()




