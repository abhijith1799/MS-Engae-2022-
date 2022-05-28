import cv2
import numpy as np
import face_recognition
import os


path = 'img'
mylist = os.listdir(path)
images = []
Names = []
print(mylist)

for i in mylist:
    Cimage = cv2.imread(f'{path}/{i}') #converting images to vectors-matrices
    images.append(Cimage) #add this matrices as a class(list)
    Names.append(os.path.splitext(i)[0])
print(Names)
#to encode all the images in the  list

def Encodings(images):
    encodelist = []
    for img in images:
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        encodelist.append(encode)
    return encodelist
EncodedlistKnown = Encodings(images)
#print(EncodedlistKnown)

#cap = cv2.VideoCapture(0)

# define a video capture object
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success, IMG = cap.read()
    CurrentIMG = cv2.resize(IMG, (0, 0), None, 0.25, 0.25,None)
    CurrentIMG = cv2.cvtColor(CurrentIMG, cv2.COLOR_BGR2RGB)

    location = face_recognition.face_locations(CurrentIMG)
    encode = face_recognition.face_encodings(CurrentIMG, location)

    for CurrentEncode, CurrentDist in zip(encode, location):
        match = face_recognition.compare_faces(EncodedlistKnown, CurrentEncode)
        Facedistance = face_recognition.face_distance(EncodedlistKnown, CurrentEncode)
        #print(list(Facedistance))
        print(len(Facedistance))
        matchIndex = np.argmin(Facedistance)
        #print(matchIndex)

        if match[matchIndex]:
            name = Names[matchIndex]
            print(name)



