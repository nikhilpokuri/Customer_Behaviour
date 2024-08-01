class CleanData:
    def clean_data(self, retail_data): 
        customers_df = retail_data.fillna({"CustomerId":0})
        return customers_df

if __name__ == "__main__":
    from pyspark.sql import SparkSession
    from data_ingestion import Session
    spark = SparkSession.builder.appName("CustomerBehaviour").getOrCreate()
    retail_data = Session().load_data(spark)
    customers_df = CleanData().clean_data(retail_data)
    customers_df.show()