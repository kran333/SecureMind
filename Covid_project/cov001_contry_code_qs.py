
def get_contry_codeqs(spark, file_path, database_name):
    table_name = 'country_code_qs'
    contry_codeqs_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)
    
    contry_codeqs_cln_df = contry_codeqs_df \
                                    .withColumnRenamed('Country', 'country') \
                                    .withColumnRenamed('Alpha-2 code', 'alpha_2_code') \
                                    .withColumnRenamed('Alpha-3 code', 'alpha_3_code') \
                                    .withColumnRenamed('Numeric code', 'numeric_code') \
                                    .withColumnRenamed('Latitude', 'latitude') \
                                    .withColumnRenamed('Longitude', 'longitude')
    print(f"################### Cleaned the {file_path} data ###########################")
    
    spark.sql(f"USE {database_name}")
    contry_codeqs_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")
    