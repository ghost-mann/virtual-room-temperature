# Virtual Room Temperature Monitoring System

A simple simulation of a smart room temperature monitor where a Python script acts as a temperature sensor publishing random temperature data to an MQTT broker. A basic Flask dashboard subscribes to the temperature topic and shows real-time updates via WebSockets.

## Features 
Simulate room temperature readings every 5 seconds.

Publish to home/temperature/reading topic via MQTT.

Flask app displays the latest temperature with a simple HTML page.

Docker Compose setup with Mosquitto, Flask app, and simulator.

