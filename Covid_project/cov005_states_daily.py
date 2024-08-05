
def get_states_daily(spark, file_path, database_name):
    table_name = 'states_daily'
    states_daily_df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)

    states_daily_cln_df = states_daily_df \
        .withColumnRenamed('probableCases', 'probable_cases') \
        .withColumnRenamed('totalTestResultsSource', 'total_test_results_source') \
        .withColumnRenamed('totalTestResults', 'total_test_results') \
        .withColumnRenamed('hospitalizedCurrently', 'hospitalized_currently') \
        .withColumnRenamed('hospitalizedCumulative', 'hospitalized_cumulative') \
        .withColumnRenamed('inIcuCurrently', 'in_icu_currently') \
        .withColumnRenamed('inIcuCumulative', 'in_icu_cumulative') \
        .withColumnRenamed('onVentilatorCurrently', 'on_ventilator_currently') \
        .withColumnRenamed('onVentilatorCumulative', 'on_ventilator_cumulative') \
        .withColumnRenamed('lastUpdateEt', 'last_update_et') \
        .withColumnRenamed('dateModified', 'date_modified') \
        .withColumnRenamed('checkTimeEt', 'check_time_et') \
        .withColumnRenamed('hospitalizedDischarged', 'hospitalized_discharged') \
        .withColumnRenamed('dateChecked', 'date_checked') \
        .withColumnRenamed('totalTestsViral', 'total_tests_viral') \
        .withColumnRenamed('positiveTestsViral', 'positive_tests_viral') \
        .withColumnRenamed('negativeTestsViral', 'negative_tests_viral') \
        .withColumnRenamed('positiveCasesViral', 'positive_cases_viral') \
        .withColumnRenamed('deathConfirmed', 'death_confirmed') \
        .withColumnRenamed('deathProbable', 'death_probable') \
        .withColumnRenamed('totalTestEncountersViral', 'total_test_encounters_viral') \
        .withColumnRenamed('totalTestsPeopleViral', 'total_tests_people_viral') \
        .withColumnRenamed('totalTestsAntibody', 'total_tests_antibody') \
        .withColumnRenamed('positiveTestsAntibody', 'positive_tests_antibody') \
        .withColumnRenamed('negativeTestsAntibody', 'negative_tests_antibody') \
        .withColumnRenamed('totalTestsPeopleAntibody', 'total_tests_people_antibody') \
        .withColumnRenamed('positiveTestsPeopleAntibody', 'positive_tests_people_antibody') \
        .withColumnRenamed('negativeTestsPeopleAntibody', 'negative_tests_people_antibody') \
        .withColumnRenamed('totalTestsPeopleAntigen', 'total_tests_people_antigen') \
        .withColumnRenamed('positiveTestsPeopleAntigen', 'positive_tests_people_antigen') \
        .withColumnRenamed('totalTestsAntigen', 'total_tests_antigen') \
        .withColumnRenamed('positiveTestsAntigen', 'positive_tests_antigen') \
        .withColumnRenamed('positiveIncrease', 'positive_increase') \
        .withColumnRenamed('negativeIncrease', 'negative_increase') \
        .withColumnRenamed('totalTestResultsIncrease', 'total_test_results_increase') \
        .withColumnRenamed('posNeg', 'pos_neg') \
        .withColumnRenamed('dataQualityGrade', 'data_quality_grade') \
        .withColumnRenamed('deathIncrease', 'death_increase') \
        .withColumnRenamed('hospitalizedIncrease', 'hospitalized_increase') \
        .withColumnRenamed('commercialScore', 'commercial_score') \
        .withColumnRenamed('negativeRegularScore', 'negative_regular_score') \
        .withColumnRenamed('negativeScore', 'negative_score') \
        .withColumnRenamed('positiveScore', 'positive_score')

    print(f"################### Cleaned the {file_path} data ###########################")

    spark.sql(f"USE {database_name}")
    states_daily_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")
    print(f"################### Loaded the {table_name} data in Hive Table ###########################")