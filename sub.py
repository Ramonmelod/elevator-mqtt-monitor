import paho.mqtt.client as mqtt

def onMensage(client, userdata, msg):
    print(msg.topic + ": " + mensage.payload.decode())


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = onMensage

client.connect("localhost",1883,60)
client.subscribe("test/status")

try:
    print("PRESS Ctrl+c to exit ...")
    client.loop_forever()
    
except:
    print("disconnecting from broker ...")

client.disconnect()