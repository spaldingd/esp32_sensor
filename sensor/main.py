"""
    main.py: executed after the boot.py file.
    Collects  DHT22 sensor reading and publishes to a MQTT topic.
"""

import time
import dht # type: ignore
from env_vars import *
import esp # type: ignore
import machine # type: ignore
import micropython # type: ignore
import network # type: ignore
from umqtt.simple import MQTTClient # type: ignore
esp.osdebug(None)
import gc
gc.collect()

# connect WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# setup pin 23 for DHT22 connection
PIN23 = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)
sensor = dht.DHT22(PIN23)

# setup the on board LED
blue_led = machine.Pin(2, machine.Pin.OUT)

# blink the on-board led 3 times
for i in range(3):
    blue_led.value(0)
    time.sleep(1)
    blue_led.value(1)
    time.sleep(1)
blue_led.value(0)

# connect to the MQTT client
client = MQTTClient(CLIENT_ID, mqtt_server, mqtt_port, mqtt_user, mqtt_password)
client.connect()

# infinite loop to collect sensor reading and publish
while True:
    try:
        blue_led.value(1)
        time.sleep(1)
        blue_led.value(0)
        t = time.localtime()
        timestamp = '{:02d}:{:02d}:{:02d}'.format(t[3], t[4], t[5])
        datestamp = '{:04d}-{:02d}-{:02d}'.format(t[0], t[1], t[2])
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        message = ("{0:10}, {1:8}, {2}, {3:3.2f}, {4:3.2f}".format(datestamp, timestamp, CLIENT_ID, temperature, humidity))
        client.publish(mqtt_topic, message)
        print(message)
    except OSError as ose:
        print("Failed to read sensor")
        print(ose)

    time.sleep(sleep_time-1)

