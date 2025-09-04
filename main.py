import RPi.GPIO as GPIO
import numpy as np
import cv2
import pickle
import time
import requests
import threading
from sensors import *

dog_face_cascade = cv2.CascadeClassifier('dog_faces.xml')
cat_face_cascade = cv2.CascadeClassifier('cat_faces.xml')
cat_recognizer = cv2.face.LBPHFaceRecognizer_create()
dog_recognizer = cv2.face.LBPHFaceRecognizer_create()

dog_recognizer.read("dog.yml")
cat_recognizer.read("cat.yml")

with open("dog.pickle", "rb") as f:
    dog_labels = pickle.load(f)
    dog_names = {v: k for k, v in dog_labels.items()}

with open("cat.pickle", "rb") as fl:
    cat_labels = pickle.load(fl)
    cat_names = {v: k for k, v in cat_labels.items()}

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[ERROR] Camera cannot be accessed!!")
    exit()

def dispense_food_and_water(animal_type):
    if animal_type == "dog":
        print("[INFO] Dispensing dog food and water...")
        openDogFood()
        time.sleep(3)
        closeDogFood()
        openWater()
        time.sleep(3)
        closeWater()
        print("[INFO] Dog food and water bowls are filled.")
    elif animal_type == "cat":
        print("[INFO] Dispensing cat food and water...")
        openCatFood()
        time.sleep(3)
        closeCatFood()
        openWater()
        time.sleep(3)
        closeWater()
        print("[INFO] Cat food and water bowls are filled.")
    
    time.sleep(5)

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Could not get frame!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    action_taken = False

    dog_faces = dog_face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)
    
    for (x, y, w, h) in dog_faces:
        dog_gray = gray[y:y+h, x:x+w]
        dogName, conf = dog_recognizer.predict(dog_gray)
        animalName1 = dog_names[dogName]

        if animalName1 == "dog":
            cv2.putText(frame, animalName1, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, cv2.LINE_AA)
            
            dogBowlWeight = getDogBowlWeight()
            waterBowlWeight = getWaterBowlWeight()

            if dogBowlWeight <= 0 and waterBowlWeight <= 0:
                thread = threading.Thread(target=dispense_food_and_water, args=("dog",))
                thread.start()
            else:
                print('[INFO] Dog food and water bowls are full. Not dispensing food and water!')
            
            action_taken = True
            break

    if not action_taken:
        cat_faces = cat_face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)
        
        for (j, k, l, m) in cat_faces:
            cat_gray = gray[k:k+m, j:j+l]
            catName, conf = cat_recognizer.predict(cat_gray)
            animalName2 = cat_names[catName]

            if animalName2 == "cat":
                cv2.putText(frame, animalName2, (j, k-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (j, k), (j + l, k + m), (255, 0, 0), 2, cv2.LINE_AA)
                
                catBowlWeight = getCatBowlWeight()
                waterBowlWeight = getWaterBowlWeight()

                if catBowlWeight <= 0 and waterBowlWeight <= 0:
                    thread = threading.Thread(target=dispense_food_and_water, args=("cat",))
                    thread.start()
                else:
                    print('[INFO] Cat food and water bowls are full. Not dispensing food and water!')

                action_taken = True
                break

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
