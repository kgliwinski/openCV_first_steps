import cv2 as cv
import numpy as np
import os

TRAIN_PATH = 'Faces/train/'
VAL_PATH = 'Faces/val/'

def create_train(p : list, haar_casc : cv.CascadeClassifier):
    features = []
    labels = []
    for person in p:
        path = os.path.join(TRAIN_PATH, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_casc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                # faces region of interest, cropping a face essentialy
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                # Just converting string to a numerical label, to decrease
                # Strain on the computer
                labels.append(label) 

    return (features, labels)


people = [i for i in os.listdir(TRAIN_PATH)]
print(people)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features, labels = create_train(people, haar_cascade)
# returning 100, 100 which is correct -> 100 faces and 100 corresponding labels
print(len(features), len(labels))

face_recognizer = cv.face.LBPHFaceRecognizer_create()

features = np.array(features, dtype='object')
labels = np.array(labels)

np.save('face_features.npy', features)
np.save('face_labels.npy', labels)

# Training the recognizer on the features list and labels
face_recognizer.train(features, labels)
# Saving the trained model
face_recognizer.save('face_trained.yml')