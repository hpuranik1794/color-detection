import cv2
from PIL import Image
from limits import get_limits

# Define yellow in BGR
yellow = [0, 255, 255]
# Capturing video through webcam
webcam = cv2.VideoCapture(0)

while True:
    # Reading the video from the webcam in image frames
    _, frame = webcam.read()

    # Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower, upper = get_limits(yellow)

    # Set mask
    mask = cv2.inRange(hsvFrame, lower, upper)

    mask_ = Image.fromarray(mask)

    # Get the bounding box coordinates
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        # Draw the rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Program Termination
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
webcam.release()

cv2.destroyAllWindows()

