import cv2 as cv
import numpy as np
import os

TRAIN_PATH = 'Faces/train/'
VAL_PATH = 'Faces/val/'

people = [i for i in os.listdir(VAL_PATH)]
print(people)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = np.load('face_features.npy', allow_pickle=True)
labels = np.load('face_labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread(VAL_PATH + 'ben_afflek/4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    cv.imshow('FACE', faces_roi)

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected face', img)

cv.waitKey(0)
