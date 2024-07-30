from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


# MongoDB connection details
mgd_db = 'emp_db'
mgd_user = 'root'
mgd_password = 'root'
mgd_host = 'localhost'
mgd_port = '27017'
mgd_coll_name = 'employee'

# HDFS details
HDFS_PATH = '/emp_project/landing_zone/'



default_args = {
    'owner': 'Kranthi',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    dag_id='001_emp_mongo_to_hdfs_extraction',
    default_args=default_args,
    description='A DAG to extract data from MongoDB employee table and store it in HDFS',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

current_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
target_dir = f"{HDFS_PATH}/{mgd_coll_name}/{current_timestamp}"

export_mongodb_data = BashOperator(
        task_id='export_mongodb_data',
        bash_command=f"""
                        mongoexport --host {mgd_host} --port {mgd_port} --db {mgd_db} --collection {mgd_coll_name} --out /tmp/{mgd_coll_name}.json
                        """,
        dag=dag)


load_data_to_hdfs = BashOperator(
        task_id='load_data_to_hdfs',
        bash_command=f"""
                        hdfs dfs -mkdir -p {target_dir}
                        hdfs dfs -put /tmp/{mgd_coll_name}.json {target_dir}""",
        dag=dag)




export_mongodb_data >> load_data_to_hdfs
