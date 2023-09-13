import sys
from Adafruit_IO import MQTTClient
import time 
import random
from simple_ai import *
from uart import *
AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "khanhmhq"
AIO_KEY = "aio_rBTU14VEl7rVhIDIOZKXNABtq5WH"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload, "Feed_ID: " + feed_id)
    if feed_id == 'button1':
        if payload == "0":
            writeData("button1-off");
        else:
            writeData("button1-on");
    if feed_id == 'button2':
        if payload == "0":
            writeData("button2-off");
        else:
            writeData("button2-on");

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5
while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     #TODO
    #     print('Publishing...')
    #     temp = random.randint(15, 60)
    #     client.publish("sensor1", temp)
    #     light = random.randint(0, 500)
    #     client.publish("sensor2", light)
    #     humi = random.randint(0, 100)
    #     client.publish("sensor3", humi)
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
            counter_ai = 5
            ai_result = image_detect()
            print("AI result: ", ai_result)
            client.publish("ai", ai_result)
        
    readSerial(client)
    time.sleep(1)
    pass