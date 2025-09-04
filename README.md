# robonimal
Developed a Raspberry Pi–based robotic system using Python and OpenCV for image processing to detect stray cats and dogs. With smart sensors, it identifies the animal type and dispenses the right amount of food and water, helping to address hunger, thirst, and malnutrition among stray animals.



# **Smart Pet Feeding and Watering Station**

This project is an automated pet feeding and watering system based on a Raspberry Pi. It uses a camera with facial recognition to identify pets (cats or dogs) and load cell weight sensors to continuously monitor the food and water bowls. When the food or water in a bowl drops below a certain threshold, the system automatically dispenses more using servo motors. This system provides a practical solution for pet owners and helps ensure their pets' consistent nutritional needs are met.

## **Features**

* **Facial Recognition:** Utilizes **OpenCV** and the **face\_recognition** library to differentiate between cats and dogs.  
* **Weight Control:** Uses **HX711 sensors** to accurately measure the weight of the food and water bowls.  
* **Automatic Dispensing:** Automatically dispenses food and water when the bowl's weight falls below a predefined threshold.  
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

1. **Hardware Connections:** Connect the sensors, motors, and camera to your Raspberry Pi according to the provided schematic.  
2. **Clone the Project:** Clone this repository to your Raspberry Pi or transfer the project files.  
3. **Run the Project:** Start the main control loop by running the following command in the terminal:  
   python3 main.py

## **Detailed Hardware Connection Diagram**

This diagram shows how the physical components of your project are connected to the Raspberry Pi. Connections are based on the pin assignments in the **sensorler.py** file.

\+---------------------------------------------------------------------------------------------------------------------+  
|                                                  Raspberry Pi GPIO Pinout                                           |  
|                                                   (BCM Pin Numbers)                                                 |  
\+---------------------------------------------------------------------------------------------------------------------+  
|                                                                                                                     |  
|                                         \+------------------------------+                                            |  
|                                         |       HX711 Sensor Modules       |                                            |  
|                                         \+------------------------------+                                            |  
|                                                                                                                     |  
|                                           V                             V                                           |  
|                                    \+-------------+               \+-------------+                                    |  
|                                    |   VCC \- 5V  |               |  GND \- GND  |                                    |  
|                                    \+-------------+               \+-------------+                                    |  
|                                                                                                                     |  
|---------------------------------------------------------------------------------------------------------------------|  
|                                                                                                                     |  
| \+--------------------------------+ \+----------------------------------+ \+----------------------------------+       |  
| | \*\*Water Bowl Sensor\*\* | | \*\*Dog Food Sensor\*\* | | \*\*Cat Food Sensor\*\* |       |  
| |                                | |                                  | |                                  |       |  
| | \*\*DT Pin:\*\* GPIO 10 (Pin 19\)   | | \*\*DT Pin:\*\* GPIO 11 (Pin 23\)     | | \*\*DT Pin:\*\* GPIO 5 (Pin 29\)      |       |  
| | \*\*SCK Pin:\*\* GPIO 9 (Pin 21\)   | | \*\*SCK Pin:\*\* GPIO 0 (Pin 27\)     | | \*\*SCK Pin:\*\* GPIO 6 (Pin 31\)     |       |  
| \+--------------------------------+ \+----------------------------------+ \+----------------------------------+       |  
|                                                                                                                     |  
| \+--------------------------------+ \+----------------------------------+ \+----------------------------------+       |  
| | \*\*Water Tank Sensor\*\* | | \*\*Dog Food Tank Sensor\*\* | | \*\*Cat Food Tank Sensor\*\* |       |  
| |                                | |                                  | |                                  |       |  
| | \*\*DT Pin:\*\* GPIO 2 (Pin 3\)     | | \*\*DT Pin:\*\* GPIO 4 (Pin 7\)       | | \*\*DT Pin:\*\* GPIO 27 (Pin 13\)     |       |  
| | \*\*SCK Pin:\*\* GPIO 3 (Pin 5\)    | | \*\*SCK Pin:\*\* GPIO 17 (Pin 11\)    | | \*\*SCK Pin:\*\* GPIO 22 (Pin 15\)    |       |  
| \+--------------------------------+ \+----------------------------------+ \+----------------------------------+       |  
|                                                                                                                     |  
|---------------------------------------------------------------------------------------------------------------------|  
|                                                                                                                     |  
| \+-----------------------------------------------------------------------------------------------------------------+ |  
| | \*\*Servo Motors (Food and Water Dispensing)\*\* | |  
| | Note: The specific pins for the motors are not defined in \`main.py\`. |                                 | |  
| | A PWM (Pulse Width Modulation) capable GPIO pin should be used for servo control.                              | |  
| | Commonly used PWM pins: GPIO 12, GPIO 13, GPIO 18, GPIO 19\.                                                     | |  
| | \* Connection: Signal Pin (Motor) \-\> GPIO (e.g., GPIO 13), VCC \-\> 5V, GND \-\> GND.                                | |  
| \+-----------------------------------------------------------------------------------------------------------------+ |  
|                                                                                                                     |  
| \+-----------------------------------------------------------------------------------------------------------------+ |  
| | \*\*Raspberry Pi Camera Module\*\* | |  
| |                                                                                                                 | |  
| | The camera module connects to the dedicated \*\*CSI (Camera Serial Interface)\*\* port on the Raspberry Pi board.  | |  
| | Make sure the ribbon cable is inserted in the correct orientation.                                              | |  
| \+-----------------------------------------------------------------------------------------------------------------+ |  
\+---------------------------------------------------------------------------------------------------------------------+

## **Project Files**

* **main.py:** The main control loop of the project. It handles the camera feed, performs facial recognition, and calls the food/water dispensing functions based on the animal type.  
* **sensorler.py:** Manages the hardware connections, including sensor calibration and motor control.  
* **hx711.py:** Contains the Python class used to communicate with the HX711 sensor module.  
* **animal\_face\_recognition.py:** Creates the pickle files of animal faces for facial recognition.  
* **cat\_faces.xml & dog\_faces.xml:** OpenCV Cascade files used for facial recognition.  
* **cat.pickle & dog.pickle:** Trained datasets for facial recognition.
