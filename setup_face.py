# setup_face.py

import cv2
import face_recognition
import os
import pickle

SAVE_PATH = 'face_data'
ENCODING_FILE = os.path.join(SAVE_PATH, 'encodings.pkl')
IMAGE_PATH = os.path.join(SAVE_PATH, 'user.jpg')

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

cap = cv2.VideoCapture(0)
print("[INFO] Press 's' to save your face. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    cv2.imshow("Register Face", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb_frame)

        if boxes:
            encodings = face_recognition.face_encodings(rgb_frame, boxes)
            with open(ENCODING_FILE, 'wb') as f:
                pickle.dump(encodings[0], f)
            cv2.imwrite(IMAGE_PATH, frame)
            print(f"[INFO] Face image and encoding saved to {SAVE_PATH}/")
        else:
            print("[WARNING] No face detected. Try again.")
        break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
