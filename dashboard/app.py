from flask import Flask, render_template_string
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'broker'
app.config['MQTT_BROKER_PORT'] = 1883
mqtt = Mqtt(app)

latest_temp = 'N/A'

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global latest_temp
    latest_temp = message.payload.decode()
    
@app.route('/')
def index():
    return render_template_string(f"""
        <h1>Room Temperature Monitor</h1>
        <h2>Current Temperature: {latest_temp}°C</h2>
    """)

@app.before_first_request
def setup():
    mqtt.subscribe('home/temperature/reading')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')