from pyspark.sql import SparkSession


spark = SparkSession.builder \
                    .appName("Covid 19 Country Code QS") \
                    .enableHiveSupport() \
                    .getOrCreate()


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/CountryCodeQS.csv"

contry_codeqs_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)

contry_codeqs_cln_temp_df = contry_codeqs_df \
                                    .withColumnRenamed('Country', 'country') \
                                    .withColumnRenamed('Alpha-2 code', 'alpha_2_code') \
                                    .withColumnRenamed('Alpha-3 code', 'alpha_3_code') \
                                    .withColumnRenamed('Numeric code', 'numeric_code') \
                                    .withColumnRenamed('Latitude', 'latitude') \
                                    .withColumnRenamed('Longitude', 'longitude')


output_folder = "COVID_19_AWS_Project/stg_layer"

contry_codeqs_cln_df.write.parquet(f'{output_folder}/contry_codeqs_stg.parquet', mode = 'overwrite')

database_name = "my_database"
table_name = "my_table"

spark.sql(f"USE {database_name}")
contry_codeqs_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")