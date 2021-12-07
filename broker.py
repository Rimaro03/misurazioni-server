import random
import datetime
import json
import time
import paho.mqtt.client as mqtt

BROKER_HOST = '192.168.5.117'
TOPIC = 'sensori/misure'
PORTA_BROKER = 1883
QOS = 0
KEEPALIVE = 60
INTERVALLO = 2

client = mqtt.Client()
client.connect(BROKER_HOST, PORTA_BROKER, KEEPALIVE)
client.loop_start()


try:
    while True:
        temperatura = random.randint(0, 30)
        umidita = random.randint(0, 100)
        timestamp = int(datetime.datetime.now().timestamp())

        dati = {
            "temperatura": temperatura,
            "umidita": umidita,
            "timestamp": timestamp
        }
        jsonData = json.dumps(dati)

        client.publish(TOPIC,jsonData,QOS)

        time.sleep(INTERVALLO)
except KeyboardInterrupt:
    time.sleep(0.1)
    print("Broker killed")