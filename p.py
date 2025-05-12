from kafka import KafkaProducer
import requests
import json
import time


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



API_KEY = 'goldapi-6o3ismajvl4lh-io'  
URL = f"https://www.goldapi.io/api/XAU/EGP"  


headers = {
    "x-access-token": API_KEY
}


while True:
    try:
        response = requests.get(URL, headers=headers)
        data = response.json()

  
        print("API Response:", data)


        if 'price_gram_24k' in data:
            gold_price_24 = data['price_gram_24k']
            gold_price_21 = data['price_gram_21k']
            gold_price_18 = data['price_gram_18k']
            curr=data["currency"]
            gold_data = {
                'metal': 'Gold',
                'price_gram_24k': gold_price_24,
                'price_gram_21k': gold_price_21,
                'price_gram_18k': gold_price_18,
                'currency': 'EGP',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"Sending: {gold_data}")
            producer.send('gold_price_24', gold_data)
        else:
            print("Error: Price data not available.")

        time.sleep(600000)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
