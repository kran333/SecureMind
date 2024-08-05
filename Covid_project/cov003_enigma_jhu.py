def get_enigma_jhu(spark, file_path, database_name):
    table_name = "enigma_jhu"
    enigma_jhu_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)

    enigma_jhu_cln_df = enigma_jhu_df.filter(enigma_jhu_df.admin2.isNotNull() & enigma_jhu_df.fips.isNotNull())
    print(f"################### Cleaned the {file_path} data ###########################")
    spark.sql(f"USE {database_name}")
    enigma_jhu_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")