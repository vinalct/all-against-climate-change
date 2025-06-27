import os
import json
from datetime import datetime
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()

PROJECT = os.getenv('GCP_PROJECT')
DATASET = os.getenv('BQ_DATASET')
RAW_TABLE = os.getenv('BQ_RAW_TABLE', 'raw_weather')

CLIENT = bigquery.Client(project=PROJECT)
TABLE_ID = f"{PROJECT}.{DATASET}.{RAW_TABLE}"

def load_raw_json(raw: dict):
    row = {
        'fetched_at': datetime.utcnow().isoformat(),
        'raw_payload': json.dumps(raw),
    }

    schema = [
        bigquery.SchemaField('fetched_at', 'TIMESTAMP'),
        bigquery.SchemaField('raw_payload', 'STRING'),
    ]

    job_config = bigquery.LoadJobConfig(
        schema=schema,
        write_disposition="WRITE_APPEND",
    )

    job = CLIENT.load_table_from_json([row], TABLE_ID, job_config=job_config)
    job.result()
    print(f"Loaded 1 row into {TABLE_ID}")
