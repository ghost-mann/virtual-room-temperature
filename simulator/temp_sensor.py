import paho.mqtt.client as mqtt
import random,time


client = mqtt.Client()
client.connect("broker", 1883)

while True:
    temp = round(random.uniform(20.0, 30.0), 2)
    client.publish("home/temperature/reading", str(temp))
    print(f"Sent temperature: {temp}°C")
    time.sleep(5)