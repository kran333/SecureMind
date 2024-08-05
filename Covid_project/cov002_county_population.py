# file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/County_Population.csv"


def get_contry_population(spark, file_path, database_name):
    table_name = "county_population"
    contry_pop_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)
    contry_pop_cln_df = contry_pop_df \
                                .withColumnRenamed('Id','id') \
                                .withColumnRenamed('Id2','id2') \
                                .withColumnRenamed('County','county') \
                                .withColumnRenamed('State','state') \
                                .withColumnRenamed('Population Estimate 2018','population_estimate_2018')
    print(f"################### Cleaned the {file_path} data ###########################")
    
    spark.sql(f"USE {database_name}")
    contry_pop_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")