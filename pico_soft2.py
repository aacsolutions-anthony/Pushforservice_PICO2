import RPi.GPIO as GPIO
import urequests as requests
#POSSIBLE DIFFERENCE IN TESTING 
```
Module difference for micropython environment 
Test which works for which in testing stage
```
import time
import json
import configparser
import network

# LOAD CONFIG
config = configparser.ConfigParser()
config.read('config.ini')

# LOAD JSON PAYLOAD
with open('payload.json') as json_file:
    JSON_PAYLOAD = json.load(json_file)

# CONFIG PARSE 
BUTTON_GPIO_PIN = config.getint('DEFAULT', 'BUTTON_GPIO_PIN')
SERVER_URL = config.get('DEFAULT', 'SERVER_URL')
# CREDENTIALS 
SSID = config.get('DEFAULT', 'SSID')
PASSWORD = config.get('DEFAULT', 'PASSWORD')

# FUNCTION - CONNECT TO WIFI
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
      pass
    print('Connection successful')
    print(wlan.ifconfig())

def button_callback(channel):
    print("Button was pressed, attempting to post to server...")
    try:
        response = requests.post(SERVER_URL, json=JSON_PAYLOAD)
        if response.status_code == 200:
            print("JSON payload successfully sent to server.")
        else:
            print(f"JSON FAILED to send to server. Response code: {response.status_code}")
    except Exception as e:
        print(f"Alternative error :/ {str(e)}")

def main():
    # CONNECT TO THE WIFI NETWORK 
    connect_wifi(SSID, PASSWORD)
    
    # SET THE GPIO MODE.
    GPIO.setmode(GPIO.BCM)
    
    # SET THE GPIO PIN FOR THE BUTTON TO INPUT MODE.
    GPIO.setup(BUTTON_GPIO_PIN, GPIO.IN)
    
    # DETECT A RISING EDGE ON THE BUTTON INPUT PIN AND CALL THE CALLBACK FUNCTION.
    # RISING EDGE CALLBACK FUNCTION (IMPORTED)
    GPIO.add_event_detect(BUTTON_GPIO_PIN, GPIO.RISING, callback=button_callback, bouncetime=300)
    
    # INF LOOP INT
    try:
        while True:
            time.sleep(0.01)  # REDUCE CPU ON INF LOOP
    except KeyboardInterrupt:
        GPIO.cleanup()

# CALL MAIN
if __name__ == "__main__":
    main()

