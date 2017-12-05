# stdlib
from collections import defaultdict

# 3p
from kafka import SimpleClient, SimpleConsumer

kafka_conn = SimpleClient("192.168.208.2:9092")
consumer = SimpleConsumer(kafka_conn, "sample_check", "test-topic",
                          auto_commit=True)

for message in consumer.get_messages(count=10):
    print message.offset
    consumer.commit()
