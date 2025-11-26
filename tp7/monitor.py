import json
from kafka import KafkaConsumer

# Initialize the Consumer
consumer = KafkaConsumer(
    'iot-sensor-data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🔍 Real-Time Machine Monitoring System Launched...\n")

for message in consumer:
    data = message.value
    temp = data['temperature']
    machine = data['machine_id']

    if temp > 80:
        print(f"🔥 OVERHEAT ALERT | {machine} | Temperature: {temp}°C 🚨")
    elif temp > 50:
        print(f"🌡️ High Temperature Warning | {machine} | Temp: {temp}°C")
    else:
        print(f"✔️ {machine} operating normally | Temp: {temp}°C")
