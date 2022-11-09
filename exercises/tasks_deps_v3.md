# Write a valid DAG using just Dummy Tasks

Write a simple DAG with the following requirements:

- `dag_id`: _tasks_deps_v3_
- `start_date`: 2022-11-01
- `schedule_interval`: daily
- it does have to execute any not triggered DAG Runs

The DAG must be composed from 7 tasks where:

- task1 is the first one
- task2 and task3, depends on task1
- task4 depends on task2 and task3
- task5 and task6 depends on task4
- task7 depends on task6

For that exercise is fine to use just the `airflow.operators.dummy.DummyOperator`.

Things to remember:

 - Tasks dependencies can be done via bit right shift operator (`>>`) that has been overloaded from Airflow in order to assume that meaning.
 - Switch on the pipeline from the UI.

 ## Second part

 Imagine that the outcome of this pipeline is basically a report and you as a team
 discover that there are some errors in the DAG and you need to update/integrate the pipeline logic.
 In this case we need to add another task, let's say task8 that must depends on task7.
 
 Then you need to recreate the report also for the previous days because it was wrong.
 How do achieve that?
 
 There is no single solution here.


