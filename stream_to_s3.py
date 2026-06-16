import pandas as pd
import boto3
import time
from datetime import datetime
import uuid
import os
import random

# AWS client (uses configured credentials)
s3 = boto3.client('s3')

BUCKET = "project-ecommerce-pipeline"
PREFIX = "raw/orders/"

# Load dataset
df = pd.read_csv("final_orders.csv")

batch_size = 20

print("🚀 Starting continuous ingestion...")

while True:
    
    # Shuffle data for realistic streaming
    df = df.sample(frac=1).reset_index(drop=True)

    for i in range(0, len(df), batch_size):
        # Take batch
        batch = df.iloc[i:i+batch_size].copy()

        # Add unique identifiers (VERY IMPORTANT)
        batch["event_id"] = [str(uuid.uuid4()) for _ in range(len(batch))]
        batch["ingestion_time"] = [datetime.now() for _ in range(len(batch))]
        now = datetime.now()

        filename = f"orders_{now.strftime('%Y%m%d_%H%M%S')}_{i}.csv"
        local_path = filename

        # Save locally
        batch.to_csv(local_path, index=False)

        # Upload to S3 (partitioned structure)
        s3.upload_file(
            local_path,
            BUCKET,
            f"{PREFIX}year={now.year}/month={now.month}/day={now.day}/{filename}"
        )
        print(f"✅ Uploaded: {filename}")

        # Clean local file
        os.remove(local_path)

        # Simulate real traffic (random delay)
        time.sleep(random.randint(300, 600))  # 5–10 minutes

    print("🔁 Restarting full dataset streaming loop...")