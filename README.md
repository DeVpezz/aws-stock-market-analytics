
Real-Time Stock Market Analytics Pipeline on AWS
A fully serverless, real-time data analytics pipeline built on AWS that ingests streaming stock data, processes it in near real time, stores it in an S3 data lake, and sends automated email alerts when stock prices cross defined thresholds.

Project Overview
This project demonstrates how to design and implement an event-driven cloud architecture using AWS managed services.
It simulates real-time stock market data ingestion and showcases stream processing, serverless computing, and alerting.

 Architecture
Python Stock Producer
        ↓
Amazon Kinesis Data Streams
        ↓
AWS Lambda (Stream Processor)
        ↓
Amazon S3 (Data Lake)
        ↓
AWS Lambda (Scheduled Analysis via EventBridge)
        ↓
Amazon SNS (Email Alerts)

🛠️ Tech Stack
Amazon Kinesis Data Streams – Real-time data ingestion
AWS Lambda – Stream processing & alert logic
Amazon S3 – Data lake storage
Amazon EventBridge – Scheduled execution
Amazon SNS – Email alerts
Python, Boto3, CloudWatch

⚙️ Features
✅ Real-time stock data ingestion using Kinesis
✅ Serverless stream processing with AWS Lambda
✅ Scalable data lake using Amazon S3
✅ Scheduled stock trend analysis
✅ Automated email alerts using SNS
✅ CloudWatch-based monitoring and logging

How It Works (Step-by-Step)
Producer Application
A Python script generates mock stock data
Sends records to Amazon Kinesis in real time
Stream Processing
Lambda function consumes Kinesis records
Stores processed data in Amazon S3
Scheduled Analysis
EventBridge triggers a Lambda every 5 minutes
Lambda checks latest stock prices in S3
Alerting
If price crosses threshold → SNS sends email notification
