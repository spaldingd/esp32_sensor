ssid = 'ssid'
password = 'wifipassword'
topic_pub = b'temp_humid'

# MQTT settings and credentials
mqtt_server = '192.168.1.1'
mqtt_port = 1883
mqtt_user = "mqttuser"
mqtt_password = "mqttpassword"
mqtt_topic = "temp_humid"

# set the time between measurements
sleep_time = 60

CLIENT_ID = "bedroom_temp"

# Sensor Limit Definitions:
temperature_limit_min = 4
temperature_limit_max = 30
humidity_limit_min = 30
humidity_limit_max = 90
