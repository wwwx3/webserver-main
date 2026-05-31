# Import Library 
from machine import Pin
from dht import DHT11
from neopixel import NeoPixel
from time import sleep

# Pin setup
dht_sensor = DHT11(Pin(13))
np = NeoPixel(Pin(23),2)

np[0] = (0,0,0)
np.write()

while True:
    dht_sensor.measure()
    
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    print("TEMP:{} HUM:{}" .format(temp,humidity))
   
    sleep(1)
