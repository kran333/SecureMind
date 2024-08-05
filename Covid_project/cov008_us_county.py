# file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/us_county.csv"

def get_us_county(spark, file_path, database_name):
    table_name = "us_county"
    us_county_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)

    print(f"################### Cleaned the {file_path} data ###########################")

    spark.sql(f"USE {database_name}")
    us_county_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")