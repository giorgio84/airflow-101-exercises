from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    dag_id='task_deps_v3',
    start_date=datetime(2022, 11, 1),
    schedule_interval="@daily", # or using cron "0 0 * * *"
    catchup=True,
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


    # Second part
    # update the DAG with: task7 >> task8
    # Then you have two possibilities:
    #
    # First: rerun DAG Runs via Airflow UI clearing them 
    #
    # Second: rurun DAG Runs via Airflow CLI
    # - Enter in the scheduler docker container
    # - execute the command: `airflow dags backdill task_deps -s 2022-11-01 -e 2022-11-09`