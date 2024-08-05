#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 US County") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/us_county.csv"


# In[4]:


us_county_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[5]:


us_county_df.printSchema()


# In[6]:


us_county_df.show()


# In[7]:


us_county_df.count()


# In[ ]:




