import boto3
import json
import time
from datetime import datetime
import random

# Create Kinesis client (uses aws configure credentials)
kinesis = boto3.client(
    'kinesis',
    region_name='ap-south-1'
)

STREAM_NAME = 'stock-market-stream'

stocks = ['AAPL', 'TSLA', 'AMZN', 'GOOG']

def generate_stock_data(symbol):
    return {
        "symbol": symbol,
        "price": round(random.uniform(100, 500), 2),
        "volume": random.randint(1000, 100000),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    for stock in stocks:
        data = generate_stock_data(stock)

        response = kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(data),
            PartitionKey=stock
        )

        print("Sent:", data)
        time.sleep(2)
