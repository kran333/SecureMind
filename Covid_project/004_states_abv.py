#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 States Abv") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/states_abv.csv"


# In[5]:


states_abv_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[6]:


states_abv_df.printSchema()


# In[7]:


states_abv_df.show(10)


# In[8]:


states_abv_df.count()


# In[9]:


states_abv_cln_df = states_abv_df.withColumnsRenamed({'State': 'state', \
                                                            'Abbreviation': 'abbreviation'})


# In[10]:


states_abv_cln_df.show()


# In[1]:


database_name = "my_database"
table_name = "my_table"


# In[ ]:


spark.sql(f"USE {database_name}")
contry_codeqs_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")

