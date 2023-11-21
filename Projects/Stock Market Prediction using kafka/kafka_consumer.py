import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json

consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=['54.90.180.129:9092'],
    value_deserializer=lambda x : loads(x.decode('utf-8')))

for c in consumer:
    print(c.value)
