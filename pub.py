import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.username_pw_set(username="ufsc", password="ufsc") # change the user and the code later and finde a way for not being hardcoded
client.connect("localhost",1883,60)

client.publish("test/status","hello world from Ramon in paho",0)

client.disconnect()