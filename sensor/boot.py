"""
    boot.py: executed on boot before main.py file.
    Connects to WiFi and configures time via NTP.
"""

import env_vars
import time
from umqttsimple import MQTTClient # type: ignore
import ubinascii # type: ignore
import machine # type: ignore
import micropython # type: ignore
import network # type: ignore
import esp # type: ignore
esp.osdebug(None)
import gc
gc.collect()



client_id = ubinascii.hexlify(machine.unique_id())


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(env_vars.ssid, env_vars.password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
