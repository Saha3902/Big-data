Here is a complete **Markdown (`.md`)** file. You can save this as `media.md`. It contains all the code and commands we used, organized step-by-step so you can present it to your teacher.

***

# TP N° 7 : Apache Kafka (Docker & Python)

**Student Name:** [Your Name]
**Date:** 23/11/2025
**Environment:** Windows 10/11, Docker Desktop, Python 3.x

---

## Part 1: Installation (Single Broker)

To start Kafka without installing Java manually, I used **Docker**.

**1. File: `docker-compose.yml` (Single Broker)**
I used the stable version `7.3.2` to avoid compatibility issues.

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.3.2
    container_name: zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:7.3.2
    container_name: kafka
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

**2. Start the Environment**
```powershell
docker-compose up -d
docker ps
```

---

## Part 2: Creating a Topic & CLI Testing

**1. Create a Topic**
I entered the container to run Kafka CLI commands.
```powershell
docker exec -it kafka /bin/bash

# Inside the container:
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

**2. Test Producer and Consumer (Console)**
*Terminal 1 (Consumer - Receiver):*
```powershell
docker exec -it kafka /bin/bash
kafka-console-consumer --topic test-topic --bootstrap-server localhost:9092
```

*Terminal 2 (Producer - Sender):*
```powershell
docker exec -it kafka /bin/bash
kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
# Type messages here (e.g., "Hello Kafka")
```

---

## Part 3: IoT Project (Python)

I created a simulation of a machine sensor sending temperature data to a monitoring dashboard.

**Prerequisites:**
```powershell
pip install kafka-python
```

**1. Producer Script (`sensor.py`)**
Simulates a machine sending temperature data every 2 seconds.



**2. Consumer Script (`monitor.py`)**
Reads data and alerts if temperature > 80°C.



**3. Execution**
```powershell
# Terminal A
python sensor.py

# Terminal B
python monitor.py
```

---

