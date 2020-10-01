import cv2
import time

cap = cv2.VideoCapture(0) # 'videoName.mp4'
flame_cascade = cv2.CascadeClassifier("20IterKnifeCascade.xml")# cascade_retrain_flame.xml

while True:
    _, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = flame_cascade.detectMultiScale(image_gray, 1.3, 5)
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
        cv2.putText(image,"Knife",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,2)
    
    cv2.imshow("image", image)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
