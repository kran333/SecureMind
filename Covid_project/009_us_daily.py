#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 US Daily") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/us_daily.csv"


# In[4]:


us_daily_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[ ]:


us_daily_df.printSchema()


# In[ ]:


us_daily_df.show()


# In[ ]:


us_daily_df.count()


# In[5]:


us_daily_cln_df = us_daily_df \
    .withColumnRenamed('hospitalizedCurrently', 'hospitalized_currently') \
    .withColumnRenamed('inIcuCurrently', 'in_icu_currently') \
    .withColumnRenamed('hospitalizedCumulative', 'hospitalized_cumulative') \
    .withColumnRenamed('inIcuCumulative', 'in_icu_cumulative') \
    .withColumnRenamed('onVentilatorCurrently', 'on_ventilator_currently') \
    .withColumnRenamed('onVentilatorCumulative', 'on_ventilator_cumulative') \
    .withColumnRenamed('lastModified', 'last_modified') \
    .withColumnRenamed('totalTestResults', 'total_test_results') \
    .withColumnRenamed('dateChecked', 'date_checked') \
    .withColumnRenamed('posNeg', 'pos_neg') \
    .withColumnRenamed('deathIncrease', 'death_increase') \
    .withColumnRenamed('hospitalizedIncrease', 'hospitalized_increase') \
    .withColumnRenamed('negativeIncrease', 'negative_increase') \
    .withColumnRenamed('positiveIncrease', 'positive_increase') \
    .withColumnRenamed('totalTestResultsIncrease', 'total_test_results_increase')


# In[6]:


us_daily_cln_df.printSchema()


# In[ ]:


us_daily_cln_df.show(1)


# In[ ]:




