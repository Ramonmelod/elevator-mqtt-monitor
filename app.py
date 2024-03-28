import paho.mqtt.client as mqtt

# Configurações do MQTT Broker
broker_address = "broker.emqx.io"
broker_port = 1883

# Tópico ao qual nos inscreveremos
topic = "/fmcled/slide"

# Função de callback para quando a conexão ao broker MQTT for realizada
def on_connect(client, userdata, flags, rc):
    print("Conectado com o código de resultado: " + str(rc))
    # Inscreva-se no tópico desejado
    client.subscribe(topic)

# Função de callback para quando uma mensagem for recebida
def on_message(client, userdata, msg):
    print("Mensagem recebida do tópico " + msg.topic + ": " + str(msg.payload.decode()))

# Cria um cliente MQTT com um client_id
client_id = "unique_client_id"  # Defina um ID único para o cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Define as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conecta-se ao broker MQTT
client.connect(broker_address, broker_port)

# Inicia o loop de rede
client.loop_forever()