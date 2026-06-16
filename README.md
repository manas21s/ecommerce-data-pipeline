# 🚀 E-Commerce Real-Time Data Pipeline

## 📌 Overview
This project implements an end-to-end real-time data pipeline using AWS, Snowflake, and Power BI.
A complete real-time data pipeline built using AWS, Snowflake, and Power BI to process, transform, and visualize e-commerce data

---

## 🎯 Business Impact

This pipeline enables real-time business insights, helping organizations 
track revenue, customer behavior, and product performance efficiently.

---

## ⚙️ Architecture

<img width="1536" height="1024" alt="Designer (2)" src="https://github.com/user-attachments/assets/02b41cb6-f6bc-408e-8096-1ad51c7cc442" />


---

## 🧩 Tech Stack

- AWS S3 (Data Storage)
- AWS Lambda (Trigger)
- AWS Step Functions (Orchestration)
- AWS Glue (ETL Processing)
- Snowflake (Data Warehouse)
  - Snowpipe
  - Streams (CDC)
  - Tasks (Automation)
- Power BI (Visualization)

---

## 🔄 Workflow

1. Data generated using Python script  
2. Data stored in S3  
3. Lambda triggers Step Function  
4. Glue performs ETL  
5. Snowpipe loads data to Snowflake  
6. Streams + Tasks process incremental data  
7. Power BI visualizes KPIs  

---

## 📊 KPIs

- Total Revenue  
- Total Orders  
- Average Order Value  
- Revenue by State  
- Category Performance  
- Top Cities  

---

## 📷 Dashboard Preview

<img width="620" height="341" alt="dashboard" src="https://github.com/user-attachments/assets/fdf39793-afcc-4db1-83dc-112ca35ba545" />

---

## ✅ Features

- Real-time ingestion (Snowpipe)  
- Incremental processing (Streams)  
- Automated pipelines (Tasks & EventBridge)  
- Interactive dashboard (Power BI)  

---

## 🔐 Security

- Removed hardcoded AWS credentials
- Used environment variables for secure access

---

## 👨‍💻 Author
Manas Shukla
