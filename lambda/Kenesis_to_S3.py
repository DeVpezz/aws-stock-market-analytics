import json
import base64
import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'stock-market-data-siddharth'

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)

        file_name = f"raw/{data['symbol']}/{datetime.utcnow().isoformat()}.json"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data)
        )

    return {"status": "success"}
