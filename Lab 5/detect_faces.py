import numpy as np
import cv2
import sys

CONFIDENCE_THRESHOLD = 0.7   # at what confidence level do we say we detected a thing
PERSISTANCE_THRESHOLD = 0.25  # what percentage of the time we have to have seen a thing

sys.path.insert(0, '../../rpi-vision')
from rpi_vision.models.teachablemachine import TeachableMachine

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = TeachableMachine('models/mask-nomask-random.zip')

last_seen = [None] * 10
last_spoken = None
img = None
webCam = False

try:
    print("Trying to open the Webcam.")
    cap = cv2.VideoCapture(0)
    if cap is None or not cap.isOpened():
        raise("No camera")
    webCam = True
except:
    print(f'No Camera detected!')
    # img = cv2.imread("../data/test.jpg")
    # print("Using default image.")

while(True):
   if webCam:
      ret, img = cap.read()

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   print(f"Found {len(faces)} Faces!")
   
   for (x,y,w,h) in faces:
       img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
       roi_gray = gray[y:y+h, x:x+w]
       roi_color = img[y:y+h, x:x+w]
       
       prediction = model.predict(roi_color)[0]
       print(f'Predictions = {prediction}')
       for p in prediction:
            label, name, conf = p
            if conf > CONFIDENCE_THRESHOLD:
                print("Detected", name)

                persistant_obj = False  # assume the object is not persistant
                last_seen.append(name)
                last_seen.pop(0)

                inferred_times = last_seen.count(name)
                if inferred_times / len(last_seen) > PERSISTANCE_THRESHOLD:  # over quarter time
                    persistant_obj = True
            else:
                last_seen.append(None)
                last_seen.pop(0)
                if last_seen.count(None) == len(last_seen):
                    last_spoken = None

   if webCam:
      cv2.imshow('face-detection (press q to quit.)',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break

cv2.imwrite('faces_detected.jpg',img)
cv2.destroyAllWindows()