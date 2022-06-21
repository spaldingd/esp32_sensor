"""
    boot.py: executed on boot before main.py file.
    Connects to WiFi and configures time via NTP.
"""

from env_vars import *
import time
from umqtt.simple import MQTTClient # type: ignore
import ubinascii # type: ignore
import machine # type: ignore
import micropython # type: ignore
import network # type: ignore
import esp # type: ignore
esp.osdebug(None)
import gc
gc.collect()
import ntptime # type: ignore


client_id = ubinascii.hexlify(machine.unique_id())


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# Update Time
ntptime.settime()
time.sleep(5)
