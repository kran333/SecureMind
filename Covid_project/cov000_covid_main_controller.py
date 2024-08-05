from pyspark.sql import SparkSession
import cov001_contry_code_qs as cov001
import cov002_county_population as cov002
import cov003_enigma_jhu as cov003
import cov004_states_abv as cov004
import cov005_states_daily as cov005
import cov006_us as cov006
import cov007_usa_hospital_beds as cov007
import cov008_us_county as cov008
import cov009_us_daily as cov009
import cov010_us_states as cov010



def get_spark_object(app_name):
    spark = SparkSession.builder \
                    .appName(app_name) \
                    .enableHiveSupport() \
                    .getOrCreate()
    return spark


def main():
    database_name = "aws_project"
    main_file_path = "/home/kranthi/BigDataTraining/Datasets/awsproject/"
    spark_obj = get_spark_object('Covid 19 project Spark Object')

    # Processing CountryCodeQS data
    file_name = main_file_path+"CountryCodeQS.csv"
    cov001.get_contry_codeqs(spark_obj, file_name, database_name)

    # Processing County_Population data
    file_name = main_file_path + "County_Population.csv"
    cov002.get_contry_population(spark_obj, file_name, database_name)

    # Processing Enigma-JHU data
    file_name = main_file_path + "Enigma-JHU.csv"
    cov003.get_enigma_jhu(spark_obj, file_name, database_name)

    # Processing states_abv data
    file_name = main_file_path + "states_abv.csv"
    cov004.get_states_abv(spark_obj, file_name, database_name)

    # Processing states_daily data
    file_name = main_file_path + "states_daily.csv"
    cov005.get_states_daily(spark_obj, file_name, database_name)

    # Processing US data
    file_name = main_file_path + "us.csv"
    cov006.get_us_tbl(spark_obj, file_name, database_name)

    # Processing usa-hospital-beds data
    file_name = main_file_path + "usa-hospital-beds.json"
    cov007.get_usa_hospital_beds(spark_obj, file_name, database_name)

    # Processing us_county data
    file_name = main_file_path + "us_county.csv"
    cov008.get_us_county(spark_obj, file_name, database_name)

    # Processing us_daily data
    file_name = main_file_path + "us_daily.csv"
    cov009.get_us_daily(spark_obj, file_name, database_name)

    # Processing us_states data
    file_name = main_file_path + "us_states.csv"
    cov010.get_contry_codeqs(spark_obj, file_name, database_name)


if __name__ == "__main__":
    main()
