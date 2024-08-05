#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 US") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/us.csv"


# In[4]:


us_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[5]:


us_df.printSchema()


# In[6]:


us_df.show()


# In[7]:


us_df.count()


# In[8]:


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


# In[9]:


us_cln_df.printSchema()


# In[ ]:




