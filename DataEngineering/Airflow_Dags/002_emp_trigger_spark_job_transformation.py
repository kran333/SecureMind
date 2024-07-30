# Import necessary libraries
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Define the default arguments
default_args = {
    'owner': 'Kranthi',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    dag_id='002_emp_trigger_spark_job_transformation',
    default_args=default_args,
    description='A DAG to trigger a Spark job',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

# Define the Spark job configuration
spark_conf = {
    'spark.submit.deployMode': 'client',  # or 'cluster'
    'spark.executor.memory': '2g',
    'spark.executor.cores': '2',
    'spark.driver.memory': '1g',
}

# Define the SparkSubmitOperator
submit_spark_job = SparkSubmitOperator(
    task_id='submit_spark_job',
    application='/path/to/your/spark_job.py',  # Path to your Spark job script
    conn_id='spark_default',  # Spark connection ID
    conf=spark_conf,
    dag=dag,
)

# Define the task dependencies (if any)
submit_spark_job
