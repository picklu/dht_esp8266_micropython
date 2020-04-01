# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

import network
from dht import DHT11
from machine import Pin

import esp
import time
esp.osdebug(None)

import gc
gc.collect()

ssid = "reachman"
password = "OhReally@2019"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(14, Pin.OUT)
d = DHT11(Pin(4, Pin.IN, Pin.PULL_UP))