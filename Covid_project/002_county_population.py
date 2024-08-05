#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 County Population") \
                    .getOrCreate()


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/County_Population.csv"


# In[4]:


contry_pop_df = spark.read \
                    .option("header", "true") \
                    .option("inferSchema", "true") \
                    .csv(file_path)


# In[5]:


contry_pop_df.show(10)


# In[6]:


contry_pop_df.count()


# In[8]:


contry_pop_cln_df = contry_pop_df \
                                .withColumnRenamed('Id','id') \
                                .withColumnRenamed('Id2','id2') \
                                .withColumnRenamed('County','county') \
                                .withColumnRenamed('State','state') \
                                .withColumnRenamed('Population Estimate 2018','population_estimate_2018')


# In[8]:


contry_pop_cln_df.show()


# In[9]:


output_folder = "COVID_19_AWS_Project/stg_layer"
contry_pop_cln_df.write.parquet(f'{output_folder}/contry_pop_cln_stg.parquet', mode = 'overwrite')


# In[10]:


database_name = "my_database"
table_name = "my_table"


# In[ ]:


spark.sql(f"USE {database_name}")
contry_codeqs_cln_df.write.mode("overwrite").saveAsTable(f"{database_name}.{table_name}")

