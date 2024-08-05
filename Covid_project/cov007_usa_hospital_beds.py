# file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/usa-hospital-beds.json"


def get_usa_hospital_beds(spark, file_path, database_name):
    table_name = "usa_hospital_beds"
    usa_hospital_beds_df = spark.read.json(file_path)

    usa_hospital_beds_cln_df = usa_hospital_beds_df \
        .withColumnRenamed('ADULT_ICU_BEDS', 'adult_icu_beds') \
        .withColumnRenamed('AVG_VENTILATOR_USAGE', 'avg_ventilator_usage') \
        .withColumnRenamed('BED_UTILIZATION', 'bed_utilization') \
        .withColumnRenamed('CNTY_FIPS', 'cnty_fips') \
        .withColumnRenamed('COUNTY_NAME', 'county_name') \
        .withColumnRenamed('FIPS', 'fips') \
        .withColumnRenamed('HOSPITAL_NAME', 'hospital_name') \
        .withColumnRenamed('HOSPITAL_TYPE', 'hospital_type') \
        .withColumnRenamed('HQ_ADDRESS', 'hq_address') \
        .withColumnRenamed('HQ_ADDRESS1', 'hq_address1') \
        .withColumnRenamed('HQ_CITY', 'hq_city') \
        .withColumnRenamed('HQ_STATE', 'hq_state') \
        .withColumnRenamed('HQ_ZIP_CODE', 'hq_zip_code') \
        .withColumnRenamed('NUM_ICU_BEDS', 'num_icu_beds') \
        .withColumnRenamed('NUM_LICENSED_BEDS', 'num_licensed_beds') \
        .withColumnRenamed('NUM_STAFFED_BEDS', 'num_staffed_beds') \
        .withColumnRenamed('OBJECTID', 'object_id') \
        .withColumnRenamed('PEDI_ICU_BEDS', 'pedi_icu_beds') \
        .withColumnRenamed('Potential_Increase_In_Bed_Capac', 'potential_increase_in_bed_capac') \
        .withColumnRenamed('STATE_FIPS', 'state_fips') \
        .withColumnRenamed('STATE_NAME', 'state_name')

    print(f"################### Cleaned the {file_path} data ###########################")

    spark.sql(f"USE {database_name}")
    usa_hospital_beds_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")
