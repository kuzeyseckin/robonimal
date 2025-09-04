# **Smart Pet Feeding and Watering Station**

This project is an automated pet feeding and watering system based on a Raspberry Pi. It uses a camera with facial recognition technology to identify pets (cats or dogs). Load cell weight sensors continuously monitor the food and water bowls. When the food or water in a bowl drops below a certain threshold, servo motors are triggered to automatically dispense more. This system provides a practical solution for pet owners and helps ensure their pets' consistent nutritional needs are met.

## **Features**

* **Facial Recognition:** Utilizes **OpenCV** and the **face\_recognition** library to distinguish between cats and dogs.  
* **Weight Control:** Uses **HX711 sensors** to accurately measure the weight in the food and water bowls.  
* **Automatic Dispensing:** Automatically dispenses food and water with servo motors when the bowl's weight falls below a predefined threshold.  
* **Modular Structure:** The project is organized into separate Python files for sensors and the main control loop, which improves code readability and maintainability.  
* **Multithreading:** Dispensing actions run on a separate thread to avoid interrupting the main loop's facial recognition and sensor monitoring tasks.

## **Hardware Requirements**

* Raspberry Pi (3B, 4, or newer)  
* Raspberry Pi Camera Module  
* HX711 Weight Sensor and Load Cells  
* Servo Motors  
* Power Supply

## **Software Requirements**

Before running the project, make sure all the libraries listed in the **requirements.txt** file are installed.

pip install \-r requirements.txt

### **requirements.txt contents:**

RPi.GPIO  
numpy  
opencv-python  
pickle  
imutils  
face\_recognition

## **Setup and Usage**

1. **Hardware Connections:** Connect the sensors, motors, and camera to your Raspberry Pi according to the schematic below.  
2. **Clone the Project:** Clone this repository to your Raspberry Pi or transfer the project files.  
3. **Run the Project:** Start the main control loop by running the following command in the terminal:  
   python3 main.py

## **Detailed Hardware Connection Diagram**

### **1\. HX711 Sensor Connections**

Each HX711 sensor has 4 basic pins: DT (Data), SCK (Clock), VCC (Power), and GND (Ground). The connection to the Raspberry Pi is as follows.

* **Water Bowl Sensor**  
  * **DT Pin (Orange):** Raspberry Pi GPIO 10 (Physical Pin 19\)  
  * **SCK Pin (Yellow):** Raspberry Pi GPIO 9 (Physical Pin 21\)  
  * **VCC & GND:** Raspberry Pi 5V & GND pins  
* **Dog Food Sensor**  
  * **DT Pin (Orange):** Raspberry Pi GPIO 11 (Physical Pin 23\)  
  * **SCK Pin (Yellow):** Raspberry Pi GPIO 0 (Physical Pin 27\)  
  * **VCC & GND:** Raspberry Pi 5V & GND pins  
* **Cat Food Sensor**  
  * **DT Pin (Orange):** Raspberry Pi GPIO 5 (Physical Pin 29\)  
  * **SCK Pin (Yellow):** Raspberry Pi GPIO 6 (Physical Pin 31\)  
  * **VCC & GND:** Raspberry Pi 5V & GND pins  
* **Water Tank Sensor**  
  * **DT Pin (Orange):** Raspberry Pi GPIO 2 (Physical Pin 3\)  
  * **SCK Pin (Yellow):** Raspberry Pi GPIO 3 (Physical Pin 5\)  
  * **VCC & GND:** Raspberry Pi 5V & GND pins  
* **Dog Food Tank Sensor**  
  * **DT Pin (Orange):** Raspberry Pi GPIO 4 (Physical Pin 7\)  
  * **SCK Pin (Yellow):** Raspberry Pi GPIO 17 (Physical Pin 11\)  
  * **VCC & GND:** Raspberry Pi 5V & GND pins  
* **Cat Food Tank Sensor**  
  * **DT Pin (Orange):** Raspberry Pi GPIO 27 (Physical Pin 13\)  
  * **SCK Pin (Yellow):** Raspberry Pi GPIO 22 (Physical Pin 15\)  
  * **VCC & GND:** Raspberry Pi 5V & GND pins

### **2\. Servo Motor Connections**

Each servo motor has 3 cables: power, ground, and signal.

* **Signal Cable (Yellow/Orange):** Connect the signal cable of each motor to a GPIO pin that supports PWM (Pulse Width Modulation). Specific pins are not defined in **main.py**, but commonly used PWM pins are **GPIO 12, GPIO 13, GPIO 18, and GPIO 19**.  
* **Power Cable (Red):** Connect to the **5V** pin on the Raspberry Pi.  
* **Ground Cable (Brown/Black):** Connect to the **GND** (Ground) pin on the Raspberry Pi.

### **3\. Raspberry Pi Camera Module Connection**

The camera module connects to the dedicated **CSI (Camera Serial Interface)** port on the Raspberry Pi board. Make sure the ribbon cable is inserted in the correct orientation with the clips on the port.

## **Project Files**

* **main.py:** The main Python file containing the project's control loop. It processes the camera feed, performs facial recognition, and calls the food/water dispensing functions based on the animal type.  
* **sensorler.py:** Manages hardware connections, sensor calibration, and motor control.  
* **hx711.py:** Contains the Python class used to communicate with the HX711 sensor module.  
* **animal\_face\_recognition.py:** Creates the pickle files for animal faces.  
* **cat\_faces.xml & dog\_faces.xml:** OpenCV Cascade files used for facial recognition.  
* **cat.pickle & dog.pickle:** Trained datasets for facial recognition.
