import env_vars
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
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
