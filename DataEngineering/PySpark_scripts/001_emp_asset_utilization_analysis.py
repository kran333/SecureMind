from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, expr, datediff, current_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Asset Utilization and Depreciation Analysis") \
    .getOrCreate()

name_node_ip = "localhost:9000"

# Load data from HDFS
assets_df = spark.read.parquet(f"hdfs://{name_node_ip}/emp_project/landing_zone/Assets/20240729_140418/16d53519-1607-42ae-8809-7366cbd3f67c.parquet")
department_df = spark.read.parquet(f"hdfs://{name_node_ip}/emp_project/landing_zone/Department/20240729_140538/f4f10e07-fd4f-4820-a06b-e594ec948335.parquet")
project_df = spark.read.parquet(f"hdfs://{name_node_ip}/emp_project/landing_zone/Projects/20240729_140617/9aecd375-bf32-47ea-8976-ec67f4b640f7.parquet")
employee_df = spark.read.json(f"hdfs://{name_node_ip}/emp_project/landing_zone/employee/20240729_141305/employee.json")
utilization_opt_path = f"hdfs://{name_node_ip}/emp_project/staging_layer/assets_utlizn"
warranty_expiry_opt_path = f"hdfs://{name_node_ip}/emp_project/staging_layer/assets_warranty_expiry" 

assets_df.show()
department_df.show()
project_df.show()
employee_df.show()



# Calculate asset depreciation
# Assuming straight-line depreciation over a period of 5 years (60 months)
assets_df = assets_df.withColumn(
    "MonthsSincePurchase",
    datediff(current_date(), col("PurchaseDate")) / 30
).withColumn(
    "DepreciationRate",
    col("Cost") / 60
).withColumn(
    "DepreciatedValue",
    when(
        col("MonthsSincePurchase") >= 60, 0).otherwise(
        col("Cost") - (col("MonthsSincePurchase") * col("DepreciationRate"))
    )
)

# assets_df.show()

# Join assets with department and project
assets_department_df = assets_df.join(
    department_df,
    assets_df.AssignedTo == department_df.ManagerID,
    "left"
).select(
    "AssetID", "AssetName", "Category", "PurchaseDate", "Cost", "AssignedTo",
    "WarrantyExpiryDate", assets_df["Status"], "MacAddress",
    "DepartmentID", "DepartmentName", "Location", "MonthsSincePurchase", "DepreciationRate", "DepreciatedValue"
)

# assets_department_df.show()

assets_project_df = assets_department_df.join(
    project_df,
    assets_department_df.AssignedTo == project_df.ProjectManagerID,
    "left"
).select(
    "AssetID", "AssetName", "Category", "PurchaseDate", "Cost", "AssignedTo",
    "WarrantyExpiryDate", assets_department_df["Status"], "MacAddress",
    assets_department_df["DepartmentID"], "DepartmentName", "Location",
    "ProjectID", "ProjectName", "StartDate", "EndDate", project_df["Budget"], project_df["Status"], "MonthsSincePurchase", "DepreciationRate", "DepreciatedValue"
)
# assets_project_df.show()

# Calculate asset utilization and summarize by department and project
utilization_df = assets_project_df.groupBy(
    "DepartmentID", "DepartmentName", "ProjectID", "ProjectName"
).agg(
    expr("sum(Cost) as TotalCost"),
    expr("sum(DepreciatedValue) as TotalDepreciatedValue"),
    expr("count(AssetID) as TotalAssets"),
    expr("avg(MonthsSincePurchase) as AvgMonthsSincePurchase")
)

# utilization_df.show()

# Identify assets nearing warranty expiry
near_warranty_expiry_df = assets_project_df.filter(
    datediff(col("WarrantyExpiryDate"), current_date()) <= 30
).select(
    "AssetID", "AssetName", "Category", "PurchaseDate", "Cost",
    "AssignedTo", "WarrantyExpiryDate", "MacAddress",
    "DepartmentID", "DepartmentName", "ProjectID", "ProjectName"
)

# near_warranty_expiry_df.show()

# Show results
utilization_df.show(truncate=False)
near_warranty_expiry_df.show(truncate=False)

# Optionally, save the results back to HDFS
if utilization_df.count() > 0:
    utilization_df.write.mode("overwrite").parquet(utilization_opt_path)
else:
    print("##################################### Not Enough Data to Write for Assets Utilization #####################################")

if near_warranty_expiry_df.count() > 0:
    near_warranty_expiry_df.write.mode("overwrite").parquet(warranty_expiry_opt_path)
else:
    print("##################################### Not Enough Data to Write for Assets Warranty Expiry #####################################")

# Stop Spark session
spark.stop()
