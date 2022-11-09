from airflow import DAG
from datetime import datetime
import requests
from airflow.operators.python import PythonOperator
import logging
from requests.auth import HTTPBasicAuth

def _fetch_subscriptions(**context):
    
    logging.info(f'Execution Date: {context["execution_date"]}')
    execution_date = context['execution_date']
    ds_nodash = context['ds_nodash']
    subs_date = execution_date.strftime('%b %-d')
    logging.info(f'Subscription Date: {subs_date}')
    url = f"https://retoolapi.dev/sWvWW0/subscriptions?subscription_date_like={subs_date},"
    response = requests.get(url)
    resp_json = response.json()
    logging.info(f'Number of : {len(resp_json)}')
    with open(f"/tmp/subscriptions_v1_{ds_nodash}.json", "w") as f:
        f.write(str(resp_json))


with DAG(
    dag_id="subscriptions_v1",
    start_date=datetime(2022, 11, 1),
    schedule_interval="@daily",
    tags=["dag_concepts"]
) as dag:

    fetch_subscriptions = PythonOperator(task_id="fetch_subscriptions", python_callable=_fetch_subscriptions)
    fetch_subscriptions