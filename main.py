import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    # Convert BGR → HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Blue color range
    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([140, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.imshow("Camera", img)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()