#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 States Daily") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/states_daily.csv"


# In[4]:


states_daily_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[ ]:


states_daily_df.printSchema()


# In[ ]:


states_daily_df.show(10)


# In[5]:


states_daily_df.count()


# In[ ]:


states_daily_cln_df = states_daily_df.withColumnsRenamed({'probableCases' : 'probable_cases' , 'totalTestResultsSource' : 'total_test_results_source' , \
                                                        'totalTestResults' : 'total_test_results' , 'hospitalizedCurrently' : 'hospitalized_currently' , \
                                                        'hospitalizedCumulative' : 'hospitalized_cumulative' , 'inIcuCurrently' : 'in_icu_currently' , \
                                                        'inIcuCumulative' : 'in_icu_cumulative' , 'onVentilatorCurrently' : 'on_ventilator_currently' , \
                                                        'onVentilatorCumulative' : 'on_ventilator_cumulative' , 'lastUpdateEt' : 'last_update_et' , \
                                                        'dateModified' : 'date_modified' , 'checkTimeEt' : 'check_time_et' , \
                                                        'hospitalizedDischarged' : 'hospitalized_discharged' , 'dateChecked' : 'date_checked' , \
                                                        'totalTestsViral' : 'total_tests_viral' , 'positiveTestsViral' : 'positive_tests_viral' , \
                                                        'negativeTestsViral' : 'negative_tests_viral' , 'positiveCasesViral' : 'positive_cases_viral' , \
                                                        'deathConfirmed' : 'death_confirmed' , 'deathProbable' : 'death_probable' , \
                                                        'totalTestEncountersViral' : 'total_test_encounters_viral' , 'totalTestsPeopleViral' : 'total_tests_people_viral' , \
                                                        'totalTestsAntibody' : 'total_tests_antibody' , 'positiveTestsAntibody' : 'positive_tests_antibody' , \
                                                        'negativeTestsAntibody' : 'negative_tests_antibody' , 'totalTestsPeopleAntibody' : 'total_tests_people_antibody' , \
                                                        'positiveTestsPeopleAntibody' : 'positive_tests_people_antibody' , \
                                                        'negativeTestsPeopleAntibody' : 'negative_tests_people_antibody' , 'totalTestsPeopleAntigen' : 'total_tests_people_antigen' , \
                                                        'positiveTestsPeopleAntigen' : 'positive_tests_people_antigen' , 'totalTestsAntigen' : 'total_tests_antigen' , \
                                                        'positiveTestsAntigen' : 'positive_tests_antigen' , 'positiveIncrease' : 'positive_increase' , \
                                                        'negativeIncrease' : 'negative_increase' , 'totalTestResultsIncrease' : 'total_test_results_increase' , \
                                                        'posNeg' : 'pos_neg' , 'dataQualityGrade' : 'data_quality_grade' , \
                                                        'deathIncrease' : 'death_increase' , 'hospitalizedIncrease' : 'hospitalized_increase' , \
                                                        'commercialScore' : 'commercial_score' , 'negativeRegularScore' : 'negative_regular_score' , \
                                                        'negativeScore' : 'negative_score' , 'positiveScore': 'positive_score'})


# In[6]:


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


# In[7]:


states_daily_cln_df.printSchema()


# In[ ]:




