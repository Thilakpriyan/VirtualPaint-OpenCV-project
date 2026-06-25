import cv2
import numpy as np

cap = cv2.VideoCapture(0)
points=[]
kernel=np.ones((5,5),np.uint8)
while True:
    success, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask=cv2.erode(mask,kernel,iterations=1)
    mask=cv2.dilate(mask,kernel,iterations=1)
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            # Draw rectangle
            cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                3
            )
            # Find center point
            cx = x + w // 2
            cy = y + h // 2
            if cy <= 60:

                # CLEAR
                if 0 <= cx <= 100:
                    points.clear()

                # BLUE
                elif 110 <= cx <= 210:
                    current_color = (255, 0, 0)

                # GREEN
                elif 220 <= cx <= 320:
                    current_color = (0, 255, 0)

                # RED
                elif 330 <= cx <= 430:
                    current_color = (0, 0, 255)

            else:
                points.append((cx, cy))

            # Draw center point
            cv2.circle(
                img,
                (cx, cy),
                8,
                (0, 0, 255),
                cv2.FILLED
            )
    for i in range(1,len(points)):
        cv2.line(img,points[i-1],points[i],(0,0,255),3)


    # CLEAR
    cv2.rectangle(img, (0, 0), (100, 60), (255, 255, 255), -1)
    cv2.putText(img, "CLEAR", (10, 38),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 0),
                2)

    # BLUE
    cv2.rectangle(img, (110, 0), (210, 60), (255, 0, 0), -1)

    # GREEN
    cv2.rectangle(img, (220, 0), (320, 60), (0, 255, 0), -1)

    # RED
    cv2.rectangle(img, (330, 0), (430, 60), (0, 0, 255), -1)

    cv2.imshow("Camera", img)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        points = []

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()