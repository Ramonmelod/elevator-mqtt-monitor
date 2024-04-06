import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost",1883,60)

client.publish("test/status","hello world from Ramon in paho",0)

client.disconnect()