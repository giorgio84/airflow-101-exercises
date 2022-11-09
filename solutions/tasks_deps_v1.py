from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    dag_id='task_deps_v1',
    start_date=datetime(2022, 11, 1),
    schedule_interval=None,
    catchup=False,
    tags=['dag_concepts']
) as dag:
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')
    task4 = DummyOperator(task_id='task4')
    task5 = DummyOperator(task_id='task5')
    task6 = DummyOperator(task_id='task6')
    task7 = DummyOperator(task_id='task7')

    task1 >> [task2, task3] >> task4 >> [task5, task6]
    task6 >> task7 