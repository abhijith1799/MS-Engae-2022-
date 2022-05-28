import cv2
import os
import sys
# sys.path.insert(0,"/home/oem/PycharmProjects/pythonProject3/pythonProject3/facerecognition")
# from img import *

def face_reg():
    path = '/home/oem/PycharmProjects/pythonProject3/pythonProject3/facerecognition/img'  # specifing path where the image wats to store.

    print("Enter the name of the person")
    name = input()

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0
    # print("Enter the name of the person")
    # name = input()

    while True:
        ret, image = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", image)
        k = cv2.waitKey(1)
        if k == 27:
            # ESC pressed for quit the capture
            print("Escape hit, closing...")
            break
        elif k == 32:
            # SPACE pressed for capturing the frame
            img_name = f'{name}.jpg'.format(img_counter)
            cv2.imwrite(os.path.join(path, f'{name}.jpg'), image)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
