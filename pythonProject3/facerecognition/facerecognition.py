
import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime
from datetime import date
import sys
# sys.path.insert(0,"/home/oem/PycharmProjects/pythonProject3/pythonProject3/facerecognition")
# from img import *


def face_reco():
    print("reached")
    path = '/home/oem/PycharmProjects/pythonProject3/pythonProject3/facerecognition/img'
    images = []  # LIST CONTAINING ALL THE IMAGES
    className = []  # LIST CONTAINING ALL THE CORRESPONDING CLASS Names
    myList = os.listdir(path)
    print("Total Classes Detected:", len(myList))
    for x, cl in enumerate(myList):
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])
    print(className)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode);
        return encodeList

    # 1
    nameList = []

    encodeListKnown = findEncodings(images)
    print('Encodings Complete')

    def markAttendance(name):
        with open('/home/oem/PycharmProjects/pythonProject3/pythonProject3/facerecognition/AttendRegistry.csv', 'r+') as f:
            myDataList = f.readlines()
            
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in line:
                now = datetime.now()
                # today = date.today()
                current_date_time = datetime.now()
                # dt_string = now.strftime("%H:%M:%S")
                f.writelines(f'\n{name},{current_date_time}')
        return nameList

    cap = cv2.VideoCapture(0)
    authorization = False

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            # print(matchIndex)

            if matches[matchIndex]:
                name = className[matchIndex].upper()
                # markAttendance(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
                # 2
                list = []
                list = markAttendance(name)
                authorization = True

            else:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, 'UNAUTHORIZED', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 0.60, (255, 255, 255), 1)
                authorization = False
        cv2.imshow('webcam', img)
        cv2.waitKey(1)
        return nameList

