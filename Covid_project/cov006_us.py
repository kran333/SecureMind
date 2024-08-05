def get_us_tbl(spark, file_path, database_name):
    table_name = 'us_tbl'
    us_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)

    us_cln_df = us_df \
        .withColumnRenamed('hospitalizedCurrently', 'hospitalized_currently') \
        .withColumnRenamed('inIcuCurrently', 'in_icu_currently') \
        .withColumnRenamed('hospitalizedCumulative', 'hospitalized_cumulative') \
        .withColumnRenamed('inIcuCumulative', 'in_icu_cumulative') \
        .withColumnRenamed('onVentilatorCurrently', 'on_ventilator_currently') \
        .withColumnRenamed('onVentilatorCumulative', 'on_ventilator_cumulative') \
        .withColumnRenamed('lastModified', 'last_modified') \
        .withColumnRenamed('totalTestResults', 'total_test_results') \
        .withColumnRenamed('posNeg', 'pos_neg')

    print(f"################### Cleaned the {file_path} data ###########################")

    spark.sql(f"USE {database_name}")
    us_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")
