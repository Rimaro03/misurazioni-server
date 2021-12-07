import mysql.connector
import time
import random
import datetime

parametri = {
    'user': 'admin',
    'password': '7907',
    'host': '192.168.5.117',
    'database': 'misurazioni'
}

try:
    connessione = mysql.connector.connect(**parametri)
    cursore = connessione.cursor(dictionary=True)
except mysql.connector.Error as err:
    print(err)

try:
    while True:
        temperatura = random.randint(0, 30)
        umidita = random.randint(0, 100)
        timestamp = int(datetime.datetime.now().timestamp())

        query = "INSERT INTO misure (temperatura, umidita, timestamp) VALUES ({}, {}, {})".format(
            temperatura, umidita, timestamp)
        cursore.execute(query)
        connessione.commit()

        time.sleep(2)
except mysql.connector.Error as err:
    print(err)
except KeyboardInterrupt:
    time.sleep(0.1)
    print("Server killed!")


