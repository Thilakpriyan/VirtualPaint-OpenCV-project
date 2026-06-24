import cv2
import numpy as np

cap = cv2.VideoCapture(0)
points=[]
while True:
    success, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

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

            points.append([cx, cy])

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

    cv2.imshow("Camera", img)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        points=[]

cap.release()
cv2.destroyAllWindows()