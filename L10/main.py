import network
from time import sleep
from dht import DHT11
from machine import Pin
from neopixel import NeoPixel
import urequests
import ujson

#Wifi Credential
SSID = "Winnie"
PASSWORD = "0845147929"
SERVER = "http://192.168.1.8:5000"

#Pin setup
sensor = DHT11(Pin(13))
np = NeoPixel(Pin(23),2)

#Network setup
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID,PASSWORD)

while not wlan.isconnected():
    sleep(1)
    
print("Connected")

#Main Loop
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        payload = {
            "temperature":temp,
            "humidity": hum,
            }
        
        res = urequests.post(SERVER+"/update",json=payload)
        data = res.json
        res.close()
    except Exception as e:
        print(e)
        
    sleep(2)
    
    