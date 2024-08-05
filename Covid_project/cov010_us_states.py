# file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/us_states.csv"
def get_contry_codeqs(spark, file_path, database_name):
    table_name = "us_states"
    us_states_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)

    print(f"################### Cleaned the {file_path} data ###########################")

    spark.sql(f"USE {database_name}")
    us_states_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")
