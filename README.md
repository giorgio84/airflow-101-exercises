# Airflow 101 Exercises

_A gentle Airflow introduction_


## How to execute a section code

The best way to try Airflow and experiments with it is running it via Docker (for more complete instruction please take a look [here]()):

Be sure you have installed __Docker CE__, after that you can execute the `docker-compose.yaml` you will find in every section like below:

```
cd airflow-101-exercises
docker-compose up -d
```

---

## Containers owerview 

Docker will create all the containers needed for a basic Airflow installation with these common components in it:

 - <span style="color:lightgreen">_airflow-scheduler_</span> : schedule and monitor all the DAGS
 - <span style="color:lightgreen">_airflow-triggerer_</span> : trigger the tasks eligible to to be runned
 - <span style="color:lightgreen">_airflow-webserver_</span> : richful UI accessible browsing [http://localhost:8080]() 
 - <span style="color:lightgreen">_airflow-flower_</span> : useful UI from which you can take a look at the whole celery cluster. You can reach it via [http://localhost:5555]() 
 - <span style="color:lightgreen">_airflow-worker_</span> : run and monitor all the running tasks 
 - <span style="color:lightgreen">_redis_</span> : Message broker needed for distribute task amongs several executors (Celery executor in that specific case)
 - <span style="color:lightgreen">_postgres_</span> : Metadata DB where used from all the components for fecthing information or update these.

---

## Check containers status

In order be sure that everything is gone well checking the containers with the following command:

````
docker-compose ps
````

Beside the containers created above, the `docker-compose.xml` will create for you three different folders:
 
 - `./dags`: you can put your DAGs here
 - `./logs`: contains applicative logs
 - `./plugins`: needed if we want to create an Airflow plugin

---

## Terminate Section Code

As soon as you finish to play with a section code, you can terminate it via:

````
docker-compose down
````