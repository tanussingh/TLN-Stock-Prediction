#       By: Tanushri Singh
#       Teammates:- Nickolas, Lawrence
#       CS 6375 - Machine Learning
#  	Instructor: Anjum Chida

###################
#WHAT IT SHOULD DO:-
#This python file should read in all the data from the datafiles
#and place them in dataframes.
###################

#Import Lib
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, array_contains, mean, desc
from pyspark.sql.types import ArrayType, StringType

class DataFiles:
    #Function to help clean data files
    def cleanfile(df):
        df = df \
                .withColumnRenamed('_c0', 'datetime') \
                .withColumnRenamed('_c2', 'portland') \
                .withColumnRenamed('_c3', 'sanFrancisco') \
                .withColumnRenamed('_c4', 'seattle') \
                .withColumnRenamed('_c5', 'losAngeles') \
                .withColumnRenamed('_c6', 'sanDiego') \
                .withColumnRenamed('_c7', 'lasVegas') \
                .withColumnRenamed('_c8', 'phoenix') \
                .withColumnRenamed('_c9', 'albuquerque') \
                .withColumnRenamed('_c10', 'denver') \
                .withColumnRenamed('_c11', 'sanAntonio') \
                .withColumnRenamed('_c12', 'dallas') \
                .withColumnRenamed('_c13', 'houston') \
                .withColumnRenamed('_c14', 'kansasCity') \
                .withColumnRenamed('_c15', 'minneapolis') \
                .withColumnRenamed('_c16', 'saintLouis') \
                .withColumnRenamed('_c17', 'chicago') \
                .withColumnRenamed('_c18', 'nashville') \
                .withColumnRenamed('_c19', 'indianapolis') \
                .withColumnRenamed('_c20', 'atlanta') \
                .withColumnRenamed('_c21', 'detroit') \
                .withColumnRenamed('_c22', 'jacksonville') \
                .withColumnRenamed('_c23', 'charlotte') \
                .withColumnRenamed('_c24', 'miami') \
                .withColumnRenamed('_c25', 'pittsburg') \
                .withColumnRenamed('_c27', 'philadelphia') \
                .withColumnRenamed('_c28', 'newYork') \
                .withColumnRenamed('_c30', 'boston')
        df = df \
                .drop('_c1') \
                .drop('_c26') \
                .drop('_c29') \
                .drop('_c31') \
                .drop('_c32') \
                .drop('_c33') \
                .drop('_c34') \
                .drop('_c35') \
                .drop('_c36')
        return df

    #Read in file, rename lists and clean up data
    spark = SparkSession.builder.getOrCreate()
    #cityAttributes file
    cityAttributesDF = spark.read.option("sep", ",").csv("DataFiles/city_attributes.csv")
    cityAttributesDF = cityAttributesDF \
            .withColumnRenamed('_c0', 'city') \
            .withColumnRenamed('_c1', 'country') \
            .withColumnRenamed('_c2', 'latitude') \
            .withColumnRenamed('_c3', 'longitude')

    #Read humidity, pressure, temperature, weather, windDir, windSpeed
    humidityDF = spark.read.option("sep", ",").csv("DataFiles/humidity.csv")
    humidityDF = cleanfile(humidityDF)
    pressureDF = spark.read.option("sep", ",").csv("DataFiles/pressure.csv")
    pressureDF = cleanfile(pressureDF)
    temperatureDF = spark.read.option("sep", ",").csv("DataFiles/temperature.csv")
    temperatureDF = cleanfile(temperatureDF)
    weatherDF = spark.read.option("sep", ",").csv("DataFiles/weather_description.csv")
    weatherDF = cleanfile(weatherDF)
    windDirDF = spark.read.option("sep", ",").csv("DataFiles/wind_direction.csv")
    windDirDF = cleanfile(windDirDF)
    windSpeedDF = spark.read.option("sep", ",").csv("DataFiles/wind_speed.csv")
    windSpeedDF = cleanfile(windSpeedDF)

    #Check dataframes are set up properly
    print(cityAttributesDF.printSchema())
    print(cityAttributesDF.show())
    print(humidityDF.printSchema())
    print(humidityDF.show())
    print(pressureDF.printSchema())
    print(pressureDF.show())
    print(temperatureDF.printSchema())
    print(temperatureDF.show())
    print(weatherDF.printSchema())
    print(weatherDF.show())
    print(windDirDF.printSchema())
    print(windDirDF.show())
    print(windSpeedDF.printSchema())
    print(windSpeedDF.show())
