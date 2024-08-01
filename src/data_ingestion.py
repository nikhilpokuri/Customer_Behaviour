import os


class Session:
    def load_data(self, spark):
        # Define the path to the data file
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Online_Retail.csv')
        print(f"CSV Data is at {file_path}")

        # Load the data
        retail_data = spark.read.csv(file_path, header=True)
        return retail_data

if __name__ == "__main__":
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("CustomerBehaviour").getOrCreate()
    df = Session().load_data(spark)
    df.printSchema()
