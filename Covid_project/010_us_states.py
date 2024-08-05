#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.sql import SparkSession


# In[ ]:


spark = SparkSession.builder \
                    .appName("Covid 19 US States") \
                    .getOrCreate()


# In[ ]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/us_states.csv"


# In[ ]:


us_states_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[ ]:


us_states_df.printSchema()


# In[ ]:


us_states_df.show()

