import cv2
import pytesseract

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the variable to store the tablet name
tablet_name = ""

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR using Tesseract
    results = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    # Extract the bounding box coordinates of the text region
    for i in range(0, len(results["text"])):
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]

        text = results["text"][i]
        conf = int(results["conf"][i])

        if conf > 70:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

            # Check if the text contains the tablet name
            if "tablet" in text.lower():
                tablet_name = text

    # Display the frame with detected text
    cv2.imshow("Frame with Detected Text", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

print("Tablet name:", tablet_name)