
# 🚀 Real-Time Stock Market Analytics Pipeline on AWS

A fully **serverless, real-time data analytics pipeline** built on AWS that ingests streaming stock data, processes it in near real time, stores it in an S3 data lake, and sends automated email alerts when stock prices cross defined thresholds.

---

## 🧠 Project Overview

This project demonstrates how to design and implement an **event-driven cloud architecture** using AWS managed services.  
It simulates real-time stock market data ingestion and showcases **stream processing, serverless computing, and alerting**.

---

## 🏗️ Architecture

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

yaml
Copy code

---

## 🛠️ Tech Stack

- **Amazon Kinesis Data Streams** – Real-time data ingestion  
- **AWS Lambda** – Stream processing & alert logic  
- **Amazon S3** – Data lake storage  
- **Amazon EventBridge** – Scheduled execution  
- **Amazon SNS** – Email notifications  
- **Python (Boto3)**  
- **Amazon CloudWatch** – Logging & monitoring  

---

## ⚙️ Features

- ✅ Real-time stock data ingestion using Kinesis  
- ✅ Serverless stream processing with AWS Lambda  
- ✅ Scalable data lake using Amazon S3  
- ✅ Scheduled stock trend analysis  
- ✅ Automated email alerts using Amazon SNS  
- ✅ CloudWatch-based monitoring and logging  

---

## 📂 Project Structure

aws-stock-market-analytics/
│
├── producer/
│ └── producer.py # Python script to send stock data to Kinesis
│
├── lambda/
│ ├── kinesis_to_s3.py # Lambda to consume Kinesis and store data in S3
│ └── stock_alert.py # Lambda to check stock prices and send SNS alerts
│
├── screenshots/
│ └── architecture.png # (Optional) Architecture diagram
│
└── README.md

yaml
Copy code

---

## ▶️ How It Works

### 1️⃣ Producer Application
- A Python script generates mock stock data
- Sends records to Amazon Kinesis in real time

### 2️⃣ Stream Processing
- Lambda function consumes Kinesis records
- Stores processed data in Amazon S3

### 3️⃣ Scheduled Analysis
- EventBridge triggers a Lambda every 5 minutes
- Lambda checks latest stock prices in S3

### 4️⃣ Alerting
- If price crosses threshold → SNS sends email notification

---

## 🧪 Example Alert

Subject: Stock Price Alert
Message: 🚨 ALERT: AAPL price crossed threshold: 412.75

yaml
Copy code

---

## 🔐 Security & Best Practices

- IAM roles with **least-privilege access**
- Fully serverless (no EC2 management)
- Event-driven and scalable architecture
- Cost-efficient AWS design

---

## 🧹 Cleanup (Avoid AWS Charges)

Delete resources in this order:
1. EventBridge rule  
2. SNS topic & subscription  
3. Lambda functions  
4. Kinesis data stream  
5. S3 bucket  

---

## 📌 Resume Highlight

> Built a real-time stock market analytics pipeline on AWS using Kinesis, Lambda, S3, EventBridge, and SNS to process streaming data and trigger automated alerts.

---

## 👤 Author

**Siddharth Singh**  
📍 Varanasi, India  
💼 Aspiring Cloud / Data Engineer  

---

⭐ If you found this project helpful, feel free to star the repository!
