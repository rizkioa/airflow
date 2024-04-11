from airflow.decorators import dag, task
import pendulum
from datetime import timedelta

@dag(
    'scheduling_demo_1',
    schedule = timedelta(weeks=2),
    start_date = pendulum.datetime(2023, 3, 10),
    catchup = True
)

def scheduling_demo_1():

    @task
    def _my_task():
        print('My task')

    _my_task()

scheduling_demo_1()