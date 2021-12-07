import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC,QOS)

def on_message(client, userdata, msg):
    dati = msg.payload.decode("utf-8")
    print (dati)
    print ("-----------------------------------")

BROKER_HOST = '192.168.5.117'
TOPIC = 'sensori/misure'
PORTA_BROKER = 1883
QOS = 0
KEEPALIVE = 60

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_HOST, PORTA_BROKER, KEEPALIVE)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print ("Stop killed")