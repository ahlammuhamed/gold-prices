from flask import Flask, jsonify
from kafka import KafkaConsumer
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


consumer = KafkaConsumer(
    'gold_price_24',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


def get_latest_gold_price():
    for message in consumer:
        return message.value 

@app.route('/gold')
def get_gold_price():
    data = get_latest_gold_price()  
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
