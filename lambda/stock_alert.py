import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET_NAME = 'stock-market-data-siddharth'
TOPIC_ARN = 'arn:aws:sns:ap-south-1:077657726828:stock-alert-topic'

PRICE_THRESHOLD = 400  # alert if price > 400

def lambda_handler(event, context):
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix='raw/'
    )

    if 'Contents' not in response:
        return

    latest_file = sorted(
        response['Contents'],
        key=lambda x: x['LastModified'],
        reverse=True
    )[0]['Key']

    obj = s3.get_object(Bucket=BUCKET_NAME, Key=latest_file)
    data = json.loads(obj['Body'].read())

    if data['price'] > PRICE_THRESHOLD:
        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=f"🚨 ALERT: {data['symbol']} price is {data['price']}",
            Subject="Stock Price Alert"
        )

    return {"status": "checked"}
