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

import credentials as creds

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(creds.ssid, creds.password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

sensor = DHT11(Pin(4, Pin.IN, Pin.PULL_UP))
