from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2
from hx711 import HX711

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

water_bowl_weight = HX711(dout_pin=10, pd_sck_pin=9)
dog_bowl_weight = HX711(dout_pin=11, pd_sck_pin=0)
cat_bowl_weight = HX711(dout_pin=5, pd_sck_pin=6)

water_tank_weight = HX711(dout_pin=2, pd_sck_pin=3)
dog_food_tank_weight = HX711(dout_pin=4, pd_sck_pin=17)
cat_food_tank_weight = HX711(dout_pin=27, pd_sck_pin=22)

def calibrate_water_tank():
    error = water_tank_weight.zero()
    if error:
        raise ValueError('[ERROR] Water tank tare weight could not be measured.')
    reading = water_tank_weight.get_raw_data_mean()
    if reading:
        print('[INFO] Water tank calibrated.')
    else:
        print('[INFO] Water tank could not be calibrated.', reading)
    water_tank_ratio = (-41372) / 85
    water_tank_weight.set_scale_ratio(water_tank_ratio)

def calibrate_dog_food_tank():
    error = dog_food_tank_weight.zero()
    if error:
        raise ValueError('[ERROR] Dog food tank tare weight could not be measured.')
    reading = dog_food_tank_weight.get_raw_data_mean()
    if reading:
        print('[INFO] Dog food tank calibrated.')
    else:
        print('[INFO] Dog food tank could not be calibrated.', reading)
    
    dog_tank_ratio = ((-368035) / 702)
    dog_food_tank_weight.set_scale_ratio(dog_tank_ratio)

def calibrate_cat_food_tank():
    error = cat_food_tank_weight.zero()
    if error:
        raise ValueError('[ERROR] Cat food tank tare weight could not be measured.')
    reading = cat_food_tank_weight.get_raw_data_mean()
    if reading:
        print('[INFO] Cat food tank calibrated.')
    else:
        print('[INFO] Cat food tank could not be calibrated.', reading)
    
    cat_tank_ratio = ((-335863) / 702)
    cat_food_tank_weight.set_scale_ratio(cat_tank_ratio)

def calibrate_water_bowl():
    error = water_bowl_weight.zero()
    if error:
        raise ValueError('[ERROR] Water bowl tare weight could not be measured.')
    reading = water_bowl_weight.get_raw_data_mean()
    if reading:
        print('[INFO] Water bowl calibrated.')
    else:
        print('[INFO] Water bowl could not be calibrated.', reading)
    
    water_bowl_ratio = (-41894) / 90
    water_bowl_weight.set_scale_ratio(water_bowl_ratio)

def calibrate_dog_food_bowl():
    error = dog_bowl_weight.zero()
    if error:
        raise ValueError('[ERROR] Dog food bowl tare weight could not be measured.')
    reading = dog_bowl_weight.get_raw_data_mean()
    if reading:
        print('[INFO] Dog food bowl calibrated.')
    else:
        print('[INFO] Dog food bowl could not be calibrated.', reading)
    
    dog_bowl_ratio = (-42453) / 90
    dog_bowl_weight.set_scale_ratio(dog_bowl_ratio)

def calibrate_cat_food_bowl():
    error = cat_bowl_weight.zero()
    if error:
        raise ValueError('[ERROR] Cat food bowl tare weight could not be measured.')
    reading = cat_bowl_weight.get_raw_data_mean()
    if reading:
        print('[INFO] Cat food bowl calibrated.')
    else:
        print('[INFO] Cat food bowl could not be calibrated.', reading)
    
    cat_bowl_ratio = (-43152) / 90
    cat_bowl_weight.set_scale_ratio(cat_bowl_ratio)

def getCatBowlWeight():
    return int(cat_bowl_weight.get_weight_mean())

def getDogBowlWeight():
    return int(dog_bowl_weight.get_weight_mean())

def getWaterBowlWeight():
    return int(water_bowl_weight.get_weight_mean())

def getWaterTankWeight():
    return int(water_tank_weight.get_weight_mean())

def getDogFoodTankWeight():
    return int(dog_food_tank_weight.get_weight_mean())

def getCatFoodTankWeight():
    return int(cat_food_tank_weight.get_weight_mean())

dog_in1_pin = 12
dog_in2_pin = 16
dog_in3_pin = 20
dog_in4_pin = 21

cat_in1_pin = 25
cat_in2_pin = 8
cat_in3_pin = 7
cat_in4_pin = 1

water_in1_pin = 14
water_in2_pin = 15
water_en = 18

GPIO.setup(cat_in1_pin, GPIO.OUT)
GPIO.setup(cat_in2_pin, GPIO.OUT)
GPIO.setup(cat_in3_pin, GPIO.OUT)
GPIO.setup(cat_in4_pin, GPIO.OUT)

GPIO.setup(dog_in1_pin, GPIO.OUT)
GPIO.setup(dog_in2_pin, GPIO.OUT)
GPIO.setup(dog_in3_pin, GPIO.OUT)
GPIO.setup(dog_in4_pin, GPIO.OUT)

GPIO.setup(water_in1_pin, GPIO.OUT)
GPIO.setup(water_in2_pin, GPIO.OUT)
GPIO.setup(water_en, GPIO.OUT)

def dogStep(w1, w2, w3, w4):
    GPIO.output(dog_in1_pin, w1)
    GPIO.output(dog_in2_pin, w2)
    GPIO.output(dog_in3_pin, w3)
    GPIO.output(dog_in4_pin, w4)

def catStep(w1, w2, w3, w4):
    GPIO.output(cat_in1_pin, w1)
    GPIO.output(cat_in2_pin, w2)
    GPIO.output(cat_in3_pin, w3)
    GPIO.output(cat_in4_pin, w4)

def waterStep(w1, w2, w3):
    GPIO.output(water_in1_pin, w1)
    GPIO.output(water_in2_pin, w2)
    GPIO.output(water_en, w3)

def closeDogFood():
    for i in range(0, 150):
        time.sleep(0.01)
        dogStep(1, 0, 0, 0)
        time.sleep(0.01)
        dogStep(0, 1, 0, 0)
        time.sleep(0.01)
        dogStep(0, 0, 1, 0)
        time.sleep(0.01)
        dogStep(0, 0, 0, 1)
    dogStep(0, 0, 0, 0)

def openDogFood():
    for i in range(0,150):
        time.sleep(0.01)
        dogStep(0, 0, 0, 1)
        time.sleep(0.01)
        dogStep(0, 0, 1, 0)
        time.sleep(0.01)
        dogStep(0, 1, 0, 0)
        time.sleep(0.01)
        dogStep(1, 0, 0, 0)
    dogStep(0, 0, 0, 0)

def closeCatFood():
    for i in range(0, 150):
        time.sleep(0.01)
        catStep(1, 0, 0, 0)
        time.sleep(0.01)
        catStep(0, 1, 0, 0)
        time.sleep(0.01)
        catStep(0, 0, 1, 0)
        time.sleep(0.01)
        catStep(0, 0, 0, 1)
        time.sleep(0.01)
    catStep(0, 0, 0, 0)

def openCatFood():
    for i in range(0, 150):
        catStep(0, 0, 0, 1)
        time.sleep(0.01)
        catStep(0, 0, 1, 0)
        time.sleep(0.01)
        catStep(0, 1, 0, 0)
        time.sleep(0.01)
        catStep(1, 0, 0, 0)
        time.sleep(0.01)
    catStep(0, 0, 0, 0)

def openWater():
    waterStep(1, 0, 1)
    
def closeWater():
    waterStep(0, 0, 0)

calibrate_water_bowl()
calibrate_dog_food_bowl()
calibrate_cat_food_bowl()
calibrate_water_tank()
calibrate_dog_food_tank()
calibrate_cat_food_tank()
