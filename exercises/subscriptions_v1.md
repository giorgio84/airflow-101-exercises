# Write a DAG fetching information from an HTTP endpoint

The DAG must be fetch subscriptions from a fictitious subscriptions endpoint.
The endpoint url is the following: https://retoolapi.dev/sWvWW0/subscriptions.

You can find more information about the endpoint callable [here](https://www.npmjs.com/package/json-server#routes).

We are relying on [Retool Api Generator](https://retool.com/api-generator/), 
a very convenience service that allow us to mock REST API endpoint without any account or key.

The JSON response will appear like that:

```
[
    {
        id: int
        subscription_date:  string
        full_name: string,
        plan: string
    }
]

```

For example:

```
[
    ...
    {
        "id": 129,
        "plan": "Free Plan",
        "full_name": "Genia Macquire",
        "subscription_date": "Nov 6, 2022 8:41 AM"
    }
    ...
]
```

Write a simple DAG with the following requirements:

- `dag_id`: _subscriptions_v1_
- `start_date`: 2022-11-01
- `schedule_interval`: daily
- it does have to execute any not triggered DAG Runs


Extract daily subscriptions and store it in a file named like `/tmp/subscriptions_v1_{ds_nodash}.json` that resides on the Airflow worker node (most simple one),
where `ds_nodash` has the format: yyyyMMdd (e.g. 20221106).

After the DAGs has been scheduled and executed you should see a bunch of subscriptions json file,
one for each day.

Hints:

 - You can filter by subscription_date using an expression like `subscription_date_like=<Initial part of the date>,`. e.g. `subscription_date_like=Nov 6,`. 
 (The comma is important here otherwise Nov 1 and Nov 10 will be matched).
 
 - A `airflow.operators.python.PythonOperator` could fit in that scenario.

 - You need to parametrize your operator with the information of the scheduling interval (e.g execution_date of the task)