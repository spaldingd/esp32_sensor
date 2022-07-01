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
print("Setting time via NTP")
ntptime.settime()
time.sleep(5)
t = time.localtime()
print("System time set to " & '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(t[0], t[1], t[2], t[3], t[4], t[5]))
