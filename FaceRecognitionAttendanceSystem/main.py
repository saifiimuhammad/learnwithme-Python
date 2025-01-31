

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0)


# Load known faces
saif_image = face_recognition.load_image_file("faces/saif.jpg")
saif_encoding = face_recognition.face_encodings(saif_image)[0]

asim_image = face_recognition.load_image_file("faces/asim.jpg")
asim_encoding = face_recognition.face_encodings(asim_image)[0]


known_face_encodings = [saif_encoding, asim_encoding]
known_face_names = ["Saif", "Asim"]


# List of expected students

students = known_face_names.copy()


face_locations = []
face_encodings = []

# Get the current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")



file = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(file)


while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Recognize faces

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding) # It tells how much your face is similar to the known face

        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        # Add text on face if the person is present
        
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_COMPLEX  
            bottomLeftCornerOfText = (10, 100)
            text_position = (50, 200) 
            fontScale = 2 
            fontColor = (0, 255, 255) 
            thickness = 4  
            lineType = cv2.LINE_AA

            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M%S")
                lnwriter.writerow([name, current_time])

    
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
file.close()