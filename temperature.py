import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

for i in range(10):
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        
        val1 = str(datetime.datetime.now())
        val2 = str(result.temperature)
        val3 = str(result.humidity)
        
        headers = {
            'Content-Type': 'application/json',
        }
        #data = '{"value1":"2018/01/06 0:03:03","value2":"24","value3":"33"}'
        data = '{"value1":"' + val1 + '","value2":"' + val2 + '","value3":"' + val3 + '"}'
        response = requests.post('https://maker.ifttt.com/trigger/temperature/with/key/dZoUaA3eWWF2H0HmNNfDtb', headers=headers, data=data)
        break
    else:
        time.sleep(1)


