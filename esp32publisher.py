#this code is made to be run in an ESP32  microcontrollers with a micropython on it (micropython version: ESP32_GENERIC-20240222-v1.22.2) 
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient

#WiFi credentials
WIFI_SSID = "network_name" # here the wifi network name
WIFI_PASSWORD = "network_password" # here the wifi code credential

# Define the MQTT broker information
MQTT_BROKER = "Broker_IpAddress"  # IP address of MQTT broker
MQTT_PORT = 1883
MQTT_TOPIC = "mqtt/elevator"

# Define the client ID for MQTT
CLIENT_ID = "esp32" 

SENSOR_PIN = 2  

# Connect to WiFi
import network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi.isconnected():
    pass
print("Connected to WiFi")

# Initialize the MQTT client
mqtt_client = MQTTClient(CLIENT_ID, MQTT_BROKER, MQTT_PORT)

# Function to publish a message when the sensor detects an event
def publish_event(topic, message):
    mqtt_client.connect()
    mqtt_client.publish(topic, message)
    mqtt_client.disconnect()

# Main loop
while True:
    # Read the sensor status
    sensor_value = Pin(SENSOR_PIN, Pin.IN).value()

    # Check if the sensor is activated
    if sensor_value == 1:
        # Publish a message in json format
        publish_event(MQTT_TOPIC, '{"Elevator": "my_house","status": "available"}')
        
        # Wait for a brief moment to avoid rapid consecutive messages
        sleep(1)
    else:
        # Wait for a short period before checking the sensor again
        sleep(0.1)
