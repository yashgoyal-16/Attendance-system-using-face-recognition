import face_recognition
import csv
import numpy
import cv2
from datetime import datetime

video = cv2.VideoCapture(0)
a = int(input('Enter number of students : '))
students = []
students_encoding = []
student_name = []
student_image_address = []
for i in range(a):
    x = input("Enter Student Name: ")
    student_name.append(x)
    z = face_recognition.load_image_file(input("Enter Student image address: "))
    student_image_address.append(z)
    y = face_recognition.face_encodings(z)[0]
    students_encoding.append(y)
    students.append(x)
  

known_face_encoding = students_encoding
known_face_names = student_name

name = ''

img_location = []
img_encoding = []

now = datetime.now()
current_date = now.strftime("%y-%m-%d")

f= open(f"{current_date}.csv", "w+", newline='')
write = csv.writer(f) 
write.writerow(["Name", "Time"])
while True:
    _, frame = video.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25,fy=0.25)
    rg = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    img_location = face_recognition.face_locations(rg)
    img_encoding = face_recognition.face_encodings(rg,img_location)
    for face_encoding in img_encoding:
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
        if matches:
           best_mtch = numpy.argmin(face_distance)

        if matches[best_mtch]:
            name = known_face_names[best_mtch]
        else:
            name = 'Unknown'
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_PLAIN
            bottomLeftCornerOfText = (10, 100)
            fontColor = (255, 0, 0)
            thickness = 3
            linetype = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale=0.5, color=fontColor, thickness=thickness, lineType=linetype)
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H-%M%S")
            write.writerow([name, current_time])


    cv2.imshow("Attendence", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    


video.release()
cv2.destroyAllWindows()
f.close()
