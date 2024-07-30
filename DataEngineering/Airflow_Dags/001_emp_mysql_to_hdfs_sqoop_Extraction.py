# Import necessary libraries
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
# import subprocess

# Define the default arguments
default_args = {
    'owner': 'Kranthi',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}


# Define the DAG
dag = DAG(
    dag_id='001_mysql_to_hdfs_sqoop_extraction',
    default_args=default_args,
    description='A DAG to extract data from MySQL tables and store it in HDFS using Sqoop',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

# Define the connection details
mysql_conn_id = 13
mysql_db = 'testdb'
mysql_user = 'root'
mysql_password = 'root'
mysql_host = 'localhost'
mysql_port = '3306'

# Define the HDFS directory
hdfs_directory = '/emp_project/landing_zone'

def sqoop_cmd_maker(table_name):
    current_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    target_dir = f"{hdfs_directory}/{table_name}/{current_timestamp}"
    # os.makedirs(target_dir, exist_ok=True)
    # subprocess.run(["hdfs", "dfs", "-mkdir", "-p", target_dir], check=True)
    sqoop_cmd = f"""
                    hdfs dfs -mkdir -p {target_dir}
                    sqoop import --connect jdbc:mysql://{mysql_host}:{mysql_port}/{mysql_db} \\
                    --username {mysql_user} --password {mysql_password} \\
                    --table {table_name} --target-dir {target_dir} --as-parquetfile --compress --compression-codec snappy --m 1
                """
    return sqoop_cmd


# Define BashOperator tasks to run Sqoop commands
import_assets_table = BashOperator(
    task_id='import_assets_table',
    bash_command=sqoop_cmd_maker('Assets'),
    dag=dag,
)

import_department_table = BashOperator(
    task_id='import_department_table',
    bash_command=sqoop_cmd_maker('Department'),
    dag=dag,
)

import_projects_table = BashOperator(
    task_id='import_projects_table',
    bash_command=sqoop_cmd_maker('Projects'),
    dag=dag,
)

# Define task dependencies
import_assets_table >> import_department_table >> import_projects_table
