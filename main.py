#this code will go into the Pico Pi once its set up with micropython
#this code is a work in progress
from machine import Pin
from time import sleep
import network #handles Wifi
import urequests #handles making and servicing reuqests
import logins #allows you to stream this code while keeping your network private

#todo: devise a way to get audio from a website to send to the pi

#networker handlers
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#sets passwords
ssid = logins.iid 
password = logins.password
#connects to the wifi
wlan.connect(ssid,password)

print("Query Start")
r = urequests.get("")#connects to a website. insert a website here
print(r.content)

pin = Pin(0, Pin.IN)

def trigger():
    print("alert triggered")
    print(r.content)
 

while True:
    if pin.value() is 0:
        trigger()
        sleep(5)
        
print("You shouldn't see this")
r.close



