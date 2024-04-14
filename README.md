Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://docs.astronomer.io/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://docs.astronomer.io/cloud/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.


🎉 Congratulations on reaching the end of the module! Take a moment to review everything you have learned: 

Data Orchestration Fundamentals

Data Orchestration is the coordination and automation of data flow across various tools and systems to deliver quality data products and analytics
The path to modern data orchestration solutions like Airflow had various evolutions starting with basic time-based scheduling tools (e.g., Cron, WTS), followed by proprietary software (e.g., AutoSys, Informatica), and finally older open-source solutions (e.g., Oozie, Luigi).
Airflow for Data Orchestration

Airflow is an open-source tool for programmatically authoring, scheduling, and monitoring data pipelines.
Airflow is defined by key characteristics such as pipelines-as-code with Python, built-in observability, a large open-source community, and much more!
Airflow is used across a variety of industries, data practitioners, and use-cases.
Airflow has key considerations to account for when using it for streaming, data processing, and when it is scaled. 
Demystifying Airflow

Airflow can be used by single developers, single teams, and multi-teams. In each case, the way it is run is different.
Airflow can be run using a variety of architecture types (e.g., on-premise) and systems (e.g., cloud services)
Airflow key terms to remember:
DAG: A directed acyclical graph that represents a single data pipeline
Task: An individual unit of work in a DAG
Operator: The specific work that a Task performs 
There are three main types of operators:
Action: Perform a specific action such as running code or a bash command
Transfer: Perform transfer operations that move data between two systems
Sensor: Wait for a specific condition to be met (e.g., waiting for a file to be present) before running the next task



The diagram has the following labeled processes:

A) Data ingestion of data sources
B) Creating analytics and reporting
C) Creating new data sets and data products
D) Using MLFlow to productionize and manage predictive models

Which of the following best matches each data practitioner persona to each process in the diagram?
A) ML Engineer B) Data Engineer C) Data Scientist D) Data Analyst
A) Data Engineer B) Data Scientist C) Data Analyst D) ML Engineer
A) Data Engineer B) Data Analyst C) Data Scientist D) ML Engineer
A) Data Scientist B) Data Engineer C) ML Engineer D) Data Analyst


Review
🎉 Congratulations on reaching the end of the module! Take a moment to review everything you have learned:

Airflow Architecture

Airflow has six main components:
The web server for serving and updating the Airflow user interface.
The metadata database for storing all metadata (e.g., users, tasks) related to your Airflow instance.
The scheduler for monitoring and scheduling your pipelines.
The executor for defining how and on which system tasks are executed.
The queue for holding tasks that are ready to be executed.
The worker(s) for executing instructions defined in a task.

Airflow runs DAGs in six different steps:
The scheduler constantly scans the DAGs directory for new files. The default time is every 5 minutes.
After the scheduler detects a new DAG, the DAG is processed and serialized into the metadata database.
The scheduler scans for DAGs that are ready to run in the metadata database. The default time is every 5 seconds.
Once a DAG is ready to run, its tasks are put into the executor's queue.
Once a worker is available, it will retrieve a task to execute from the queue.
The worker will then execute the task.
DAG Components

A DAG has four core parts:
The import statements, where the specific operators or classes that are needed for the DAG are defined.
The DAG definition, where the DAG object is called and where specific properties, such as its name or how often you want to run it, are defined.
The DAG body, where tasks are defined with the specific operators they will run.
The dependencies, where the order of execution of tasks is defined using the right bitshift operator (>>) and the left bitshift operator (<<).

A DAG’s task can be defined as being either upstream or downstream to another task.

Review
🎉 Congratulations on reaching the end of the module! Take a moment to review everything you have learned:

Install Airflow

There are two primary ways to install Airflow on a local machine: Python Package Index or Containerization Solutions (e.g., Docker, Podman)
The Python Package Index
This method is great for anyone who is comfortable with Python and Python environments or may only have access to it in their local environment 
This method does require quite a bit of manual setup to get Airflow working on a local machine
Containerization Solutions
This method is great for anyone familiar or already using a containerization solution
This method may still require a bit of customization to the container if the Airflow installation needs to be fine-tuned
The Astro CLI is an open-source command line interface (CLI) that makes setting up, running, and managing Airflow a breeze. It comes built-in with a handful of features to make it easier to get started quicker. 
Alternatives to the Astro CLI include using the Airflow CLI, which is built-in to Airflow, or another open-source project called AirflowCTL
Astro CLI can be installed on Mac, Windows, and Linux machines by following the instructions listed in the documentation.
Set up and Run an Airflow Project

To set up a new Airflow project with the Astro CLI, make a new folder, and then use the command astro dev init to generate a new project.
The Astro CLI will generate a project with a standard project directory. This includes:
The dags directory: Contains Python files corresponding to data pipelines, including examples such as example_dag_advanced and example_dag_basic.
The include directory: Used for storing files like SQL queries, bash scripts, or Python functions needed in data pipelines to keep them clean and organized.
The plugins directory: Allows for the customization of the Airflow instance by adding new operators or modifying the UI.
The tests directory: Contains files for running tests on data pipelines, utilizing tools like the pytest library.
The .dockerignore file: Describes files and folders to exclude from the Docker image during the build.
The .env file: Used for configuring Airflow instances via environment variables.
The .gitignore file: Specifies files and folders to ignore when pushing the project to a git repository, useful for excluding sensitive information like credentials.
The airflow_settings.yaml file: Stores configurations such as connections and variables to prevent loss when recreating the local development environment.
The Dockerfile: Used for building the Docker image to run Airflow, with specifications for the Astro runtime Docker image and the corresponding Airflow version.
The packages.txt file: Lists additional operating system packages to install in the Airflow environment.
The README file: Provides instructions and information about the project.
The requirements.txt file: Specifies additional Python packages to install, along with their versions, to extend the functionality of the Airflow environment.
The Astro CLI can be used to run an Airflow project. To start an Airflow project with the Astro CLI, use the command astro dev start. To restart the project, use astro dev restart, and to stop the project, use the command astro dev stop.
To get Airflow to work with VSCode and provide benefits like correct syntax highlighting and autocompletion, the VSCode instance must be run inside of the docker container using the Dev Containers extension.

Summary
Thank you for joining us in this module on Airflow UI

We explored the Airflow UI, where Airflow's DAGs View is the first page users see upon logging in, providing a comprehensive list of all the data pipelines in the Airflow instance.
This view displays various columns, including DAG ID, tags, scheduling interval, previous and current DAG Run statuses, most recent task states, and actions to delete or trigger the DAG.
Different views, such as the grid, graph, calendar, landing time, Gantt, and code views, are available for each DAG, allowing users to monitor and manage their DAG Runs and tasks.
The grid view presents a history of task, and DAG Run states for a particular DAG, while the graph view visually represents task dependencies.
The calendar view helps identify patterns in DAG Runs, and the landing time view helps optimize task completion times.
The Gantt view helps identify bottlenecks and latency between tasks.
The code view allows users to access the serialized code of the data pipeline stored in the database, verifying if modifications made to the pipeline are being used by the scheduler.
In case of task failure, users can go to the grid or graph view, access the failed task logs, fix the error, and rerun the task.
Users can also access the list of all DAG Runs or task instances in the Airflow instance by going to Browse and then DAG Runs or Task Instances.
Users can filter the list by adding filters such as DAG ID and select the DAG Runs or task instances they want to rerun or delete.
We also learned that it is recommended to manually delete metadata such as DAG Runs and task instances every 28 days to avoid affecting the scheduler.
Thank you for tuning in. See you in the next one.

Wrap Up
Well done!
Here are the key takeaways from this module:

A DAG must have a unique identifier and a start_date with a datetime object
The schedule interval is optional and defines the trigger frequency of the DAG
Defining a description, the catchup parameter to avoid running past non-triggered DAG runs, and tags to filter is strongly recommended.
To create a task, look at the https://registry.astronomer.io/ first.
A task must have a unique identifier within a DAG
You can specify default parameters to all tasks with default_args that expects a dictionary
Define dependencies with bitshift operators (>> and <<) as well as lists.
chain helps to define dependencies between task lists

Summary
Thank you for joining us in this module on DAG scheduling.

We learnt about the states of a DAGRun which initially is Queued, and changes to Running as soon as the first task runs. Once all tasks are completed, the final state of the DAGRun is determined by the state of the leaf tasks, which could be Success or Failure.
The start date and scheduling interval are two important parameters to consider when scheduling a DAG. DAGRuns are created based on these parameters and have a data interval start and end corresponding to the time frame for which the DAG was executed.
The start date parameter defines the timestamp from which the scheduler will attempt to backfill, and the scheduling interval determines how often a DAG runs.
The catchup mechanism in Airflow allows running all non-triggered DAGRuns between the start date and the last time the DAG was triggered. The backfilling mechanism allows running historical DAGRuns or rerun already existing DAGRuns.
We also explored the Airflow CLI commands to backfill our DAG for any data intervals, regardless of the start date of our data pipeline.
Users can define the scheduling interval using CRON expressions or timedelta object, and can use a timetable to schedule a DAG more precisely.
It is important to set the start date parameter properly to avoid confusion with Airflow, and use a static date.
Thank you for tuning in. See you in the next one.

Summary
Key Takeaway Summary

An Airflow Connection stores credentials to interact with external systems (S3, Snowflake, etc).
A Connection is a set of parameters such as login, password, host and some specific fields that depend on the Connection type.
A Connection type corresponds to the external system you want to interact with: Snowflake, Postgres, MySQL etc.
If the Connection type isn't available, you must install the corresponding Airflow provider.
A Connection must have a unique identifier.
To use a Connection in an Operator, refer to it using the Connection identifier.

Summary
Thank you for joining us in this module on XCOMs

We learnt about XCOMs, a native feature of Airflow, that enables the sharing of data between tasks by using the Airflow meta database.
To use XCOM, a DAG and task must first be created, and then an XCOM can be created by returning a value from a task that can be retrieved by another task.
The XCOM has a key, value, timestamp, task ID, and DAG ID, and must be JSON serializable.
Using the xcom_push and xcom_pull methods in Airflow, one can define a specific key to an XCOM, giving flexibility in defining task IDs and allowing for pulling data from multiple tasks simultaneously.
The Airflow UI can display XCOMs and their properties, and XCOMs can be used to share small amounts of metadata between tasks.
However, XCOMs have limitations based on the database used, with SQLite allowing up to 2GB, Postgres up to 1GB, and MySQL up to 64KB.
It is not suitable for sharing large amounts of data, and for that, one should trigger a Spark job or similar.
In summary, XCOMs are a useful feature of Apache Airflow for sharing small amounts of data between tasks, but it is important to understand their limitations and use them accordingly.
Thank you for tuning in. See you in the next one.

Summary
Thank you for joining us in this module on Airflow Variables

We learnt how the use of variables in programming can simplify and streamline code by storing information that can be used across multiple tasks or functions. Variables consist of a unique identifier, a value that is JSON serializable.
They can be created, edited, deleted, or exported and can also be stored in a secret backend or by using environment variables.
For sensitive values, Airflow allows for the creation of hidden variables by specifying certain keywords such as "api_key", "password", or "secret" in the key. These variables remain hidden on the Airflow UI even when edited, providing a safe way to store sensitive information.
In addition, Airflow variables can be created by exporting environment variables with the prefix "AIRFLOW_VAR". This method allows for keeping sensitive values hidden from the Airflow UI, faster processing, and easy versioning of variables as they are stored in a file.
While these variables cannot be seen on the Airflow UI, they can still be used in DAGs.
Overall, the use of variables in Airflow can simplify code, improve efficiency, and provide a safe way to store sensitive information.
Thank you for tuning in. See you in the next one.

Summary
Thank you for joining us in this module on debugging DAGS in Airflow. 
We have learned some valuable techniques that will help you identify and resolve issues that may arise when working with Airflow. 
Firstly, we looked at the basic checks that we can perform on our Airflow settings such as checking the wait intervals and the scaling parameters for our DAG.
We then learned how to validate that our DAGs and modules are present at the correct location and our DAG has been instantiated properly and that any dependencies are resolved correctly.
Next, we explored how to check the health and logs of our scheduler to make sure our DAGs have been parsed and are being scheduled properly.
We also learned how to verify the integrity of external systems that our DAGs may interact with, such as databases, and discussed the necessity to verify whether these systems allow connections to be established.
Finally, we also looked at how to resolve dependency conflicts between various DAGs by using operators such as the KubernetesPodOperator, the ExternalPythonOperator, or the PythonVirtualEnvironment operator. These three operators allow us to isolate our DAG and any of its dependencies from our main Airflow to avoid any conflicts that may arise.
 
With these techniques, we can ensure that our DAGs run smoothly and that any issues that may arise can be quickly identified and resolved.
Thank you for tuning in and happy debugging. 


Practice: Better utilize Sensors
Introduction
Sensors are designed to wait for something to happen.

By default, a sensor waits for 7 days before timing out, which can lead to an issue... Not being able to run any more tasks!

In this activity, you will learn:

Best practices around Sensors
How to avoid freezing your entire Airflow instance
Better optimize resources to execute more tasks and lower your infra costs
Prerequisites
To follow the activity, you have two options:

Running a Sandbox environment in the Cloud with Github Codespaces (Github account required)
Running a local development environment with the Astro CLI
To set up your environment, go to the following repo and look at the Readme
https://github.com/astronomer/education-sandbox
Ready? let's go!

Practice
To show you what happens if you run too many Sensors without being careful with your resources, open .env and add the following value:

AIRFLOW__CORE__PARALLELISM=3
 
This environment variable overwrites the parallelism to limit the maximum number of concurrent tasks to 3. That means you can't have more than 3 tasks running in parallel.
 

In the folder dags, create a new file fist_dag.py

from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['sensor'],
    catchup=False
)
def first_dag():

    wait_for_files = FileSensor.partial(
        task_id='wait_for_files',
        fs_conn_id='fs_default',
    ).expand(
        filepath=['data_1.csv', 'data_2.csv', 'data_3.csv']
    )

    @task
    def process_file():
        print("I processed the file!")

    wait_for_files >> process_file()

first_dag()
This DAG runs three FileSensor, each waiting for data_1.csv, data_2.csv, and data_3.csv, respectively.

Since the FileSensor needs a connection that contains the path where the files we're waiting for will be, we must create this connection fs_default

Open airflow_settings.yaml and create the following connection

airflow:
  connections:
    - conn_id: fs_default
      conn_type: File (path) 
      conn_host:
      conn_schema:
      conn_login:
      conn_password:
      conn_port:
      conn_extra:
        path: /usr/local/airflow/include/
Finally, create new file second_dag.py in the folder dags

from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['sensor'],
    catchup=False
)
def second_dag():

    @task
    def runme():
        print("Hi")

    runme()

second_dag()
 

Once you have everything set up, restart the Airflow instance with astro dev restart in the terminal.

 

Exercises



Best practices with Sensors
When using sensors, keep the following in mind to avoid potential performance issues:

Always define a meaningful timeout parameter for your sensor. The default for this parameter is seven days, which is a long time for your sensor to be running. When you implement a sensor, consider your use case and how long you expect the sensor to wait and then define the sensor's timeout accurately.
Whenever possible and especially for long-running sensors, use the reschedule mode so your sensor is not constantly occupying a worker slot. This helps avoid deadlocks in Airflow where sensors take all of the available worker slots.
If your poke_interval is very short (less than about 5 minutes), use the poke mode. Using reschedule mode in this case can overload your scheduler.
Define a meaningful poke_interval based on your use case. There is no need for a task to check a condition every 60 seconds (the default) if you know the total amount of wait time will be 30 minutes.



Wrap up
Key takeaways:

Sensors wait for an event/condition to be met to complete
By default, a Sensor times out after 7 days. You should define a better value with the timeout parameter
A sensor checks an event/condition at every poke_interval (60 seconds by default)
While a sensor waits, it continuously takes a work slot
If you have many sensors or expect them to take time before complete, use the reschedule mode
With the reschedule mode, while a sensor is waiting, its status will be up_for_reschedule
You can create a sensor with @task.sensor 


docker exe -it idporject bash

astro dev bash

Summary
Thank you for joining us in this module on Airflow CLI.

We explored various ways of running the Airflow CLI
We learnt the commands that are necessary while getting started with Airflow
We also learnt how the CLI commands help us understand our Airflow environment better
And also how how knowing about our environment  can help us debug tasks
We also learnt how to export and import settings from an Airflow environment
Not to forget we learnt about the backfill command which can be tricky to execute if we don't have access to the CLI.
And finally along with finding errors in our DAGs we also learnt to test our tasks.
Airflow CLI is a very useful tool and gives you the options that are not there on the UI.

airflow cheat-sheet

References
References

1. Local Development Environment - https://academy.astronomer.io/local-development-environment
2. Environment Variables - https://academy.astronomer.io/astro-module-environment-variables
3. Airflow Configuration - https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
4. CLI Commands - https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html
5. Astro CLI - https://docs.astronomer.io/astro/cli/reference
6. Airflow Variables - https://academy.astronomer.io/astro-runtime-variables-101
7. Airflow Connections - https://academy.astronomer.io/connections-101 
8. Debugging DAGs - https://academy.astronomer.io/debug-dags
