from airflow import DAG
from datetime import datetime
import requests
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
import logging
from requests.auth import HTTPBasicAuth
import json
import ast

def _process_subscriptions(ds_nodash):
    with open(f"/tmp/subscriptions_v2_{ds_nodash}.json", "r") as f:
        parsed_json = ast.literal_eval(f.read())
        logging.info(f'Subscriptions processed: {len(parsed_json)}')


with DAG(
    dag_id="subscriptions_v2",
    start_date=datetime(2022, 11, 1),
    schedule_interval="@daily",
    tags=["dag_concepts"]
) as dag:

    
    wait_subscriptions = FileSensor(task_id="wait_subscriptions",
                                   filepath="/tmp/subscriptions_v2_{{ ds_nodash }}.json",
                                   poke_interval=30,
                                   mode="reschedule")

    process_subscriptions = PythonOperator(task_id="process_users",
                                           python_callable=_process_subscriptions)

    wait_subscriptions >> process_subscriptions