# 🚀 E-Commerce Real-Time Data Pipeline

## 📌 Overview
This project implements an end-to-end real-time data pipeline using AWS, Snowflake, and Power BI.

---

## ⚙️ Architecture
---

## 🧩 Tech Stack

- AWS S3
- AWS Lambda
- Step Functions
- AWS Glue
- Snowflake (Snowpipe, Streams, Tasks)
- Power BI

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

## 👨‍💻 Author
Manas Shukla
