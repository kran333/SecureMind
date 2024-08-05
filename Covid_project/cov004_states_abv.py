
def get_states_abv(spark, file_path, database_name):
    table_name = "state_abbreviation"
    states_abv_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)

    states_abv_cln_df = states_abv_df\
                                .withColumnRenamed('State', 'state') \
                                .withColumnRenamed('Abbreviation', 'abbreviation')
    print(f"################### Cleaned the {file_path} data ###########################")
    spark.sql(f"USE {database_name}")
    states_abv_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")
