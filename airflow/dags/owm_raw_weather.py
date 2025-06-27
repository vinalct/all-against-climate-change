import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='owm_raw_etl',
    default_args=DEFAULT_ARGS,
    description='Fetch raw JSON from OpenWeatherMap and load into BigQuery',
    schedule_interval='0 * * * *',
    start_date=datetime(2023, 12, 30),
    catchup=False,
    tags=['owm', 'raw', 'bigquery'],
) as dag:

    def extract(**context):
        from src.extract.openweathermap import fetch_weather
        raw = fetch_weather()
        context['ti'].xcom_push(key='raw_json', value=raw)

    def load(**context):
        from src.load.to_bigquery import load_raw_json
        raw = context['ti'].xcom_pull(key='raw_json', task_ids='extract')
        load_raw_json(raw)

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    extract_task >> load_task
