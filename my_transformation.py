import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *




###Bookings data

@dlt.table(name = "stage_bookings")

def stage_bookings():
    df = spark.readStream.format("delta")\
        .load("/Volumes/workspace/bronze/bronze_volume/bookings/data")          
    return df

@dlt.view(name = "trans_bookings")

def trans_bookings():
    df = spark.readStream.table("stage_bookings")
    df = df.withColumn("amount", col("amount").cast(DoubleType())) \
        .withColumn("booking_date", to_date(col("booking_date")))\
        .withColumn("modified_date", current_timestamp())\
        .drop("_rescued_data")
              
    return df

rules ={
    "rule1": "booking_id IS NOT NULL",
    "rule2": "passenger_id IS NOT NULL",
    "rule3": "flight_id IS NOT NULL",
    "rule4": "airport_id IS NOT NULL",
    "rule5": "amount IS NOT NULL"
}


@dlt.table(name = "silver_bookings")

@dlt.expect_all_or_drop(rules)
def trans_bookings():
    df = spark.readStream.table("trans_bookings")
              
    return df


######################################################


##flights data


@dlt.view(name = "transform_flights")

def transform_flights():
    df = spark.readStream.format("delta")\
        .load("/Volumes/workspace/bronze/bronze_volume/flights/data/")

    df = df.withColumn("flight_date", to_date(col("flight_date")))\
        .withColumn("modified_date", current_timestamp())\
        .drop("_rescued_data")

    return df

dlt.create_streaming_table(name = "silver_flights")

dlt.create_auto_cdc_flow(
    target = "silver_flights",
    source = "transform_flights",
    keys = ["flight_id"],
    sequence_by= col("modified_date"),
    stored_as_scd_type = 1
)



######################################################
##passenger data


@dlt.view(name = "transform_passengers")

def transform_passengers():
    df = spark.readStream.format("delta")\
        .load("/Volumes/workspace/bronze/bronze_volume/customers/data/")
    df = df.withColumn("modified_date", current_timestamp())\
        .drop("_rescued_data")

    return df

dlt.create_streaming_table(name = "silver_passengers")

dlt.create_auto_cdc_flow(
    target = "silver_passengers",
    source = "transform_passengers",
    keys = ["passenger_id"],
    sequence_by= col("modified_date"),
    stored_as_scd_type = 1
)

######################################################

##Airports data


@dlt.view(name = "transform_airports")

def transform_airports():
    df = spark.readStream.format("delta")\
        .load("/Volumes/workspace/bronze/bronze_volume/airport/data/")
    df = df.withColumn("modified_date", current_timestamp())\
        .drop("_rescued_data")

    return df

dlt.create_streaming_table(name = "silver_airports")

dlt.create_auto_cdc_flow(
    target = "silver_airports",
    source = "transform_airports",
    keys = ["airport_id"],
    sequence_by= col("modified_date"),
    stored_as_scd_type = 1
)
######################################################

##Silver Layer Business View

@dlt.table(name = "silver_layer")

def silver_layer():
    df = spark.readStream.table("silver_bookings")\
        .join(dlt.readStream("silver_flights"), ["flight_id"])\
        .join(dlt.readStream("silver_passengers"), ["passenger_id"])\
        .join(dlt.readStream("silver_airports"), ["airport_id"])\
        .drop("modified_date")

    return df

