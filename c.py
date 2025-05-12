from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    'gold_price_24',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Waiting for gold price data...")
try:
    for message in consumer:
        data = message.value
        print(f"Metal: {data['metal']}, gram_24k: {data['price_gram_24k']}, gram_21k: {data['price_gram_21k']}, gram_18:{data['price_gram_18k']} {data['currency']}, Timestamp: {data['timestamp']}")
except KeyboardInterrupt:
    print("program End")
    consumer.close()
