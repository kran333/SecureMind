#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 Enigma JHU") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/Enigma-JHU.csv"


# In[4]:


contry_pop_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[10]:


contry_pop_df.printSchema()


# In[21]:


contry_pop_df.show(10)


# In[6]:


contry_pop_df.count()


# In[19]:


null_cols_df = contry_pop_df.filter(contry_pop_df.admin2.isNull() & contry_pop_df.fips.isNull())


# In[20]:


null_cols_df.count()


# In[1]:


database_name = "my_database"
table_name = "my_table"


# In[ ]:


spark.sql(f"USE {database_name}")
contry_codeqs_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")

