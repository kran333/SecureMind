#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder \
                    .appName("Covid 19 USA Hospital Beds") \
                    .getOrCreate()


# In[ ]:


spark


# In[3]:


file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/usa-hospital-beds.json"


# In[4]:


usa_hospital_beds_df = spark.read.json(file_path)


# In[ ]:


usa_hospital_beds_df.printSchema()


# In[ ]:


usa_hospital_beds_df.show(5)


# In[ ]:


usa_hospital_beds_df.count()


# In[5]:


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


# In[6]:


usa_hospital_beds_cln_df.printSchema()


# In[ ]:




