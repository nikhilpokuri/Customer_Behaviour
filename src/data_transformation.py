from pyspark.sql.functions import format_number, col, to_timestamp


class TransformData:
    def transform_data(self, customers_df):
        # Example transformation
        customers_df = customers_df.withColumn("TotalPrice", format_number(col("UnitPrice")*col("Quantity"), 3))
        customers_df = customers_df.withColumn("InvoiceDate", to_timestamp(col("InvoiceDate"), "dd-MM-yyyy HH:mm"))
        return customers_df

if __name__ == "__main__":
    from data_cleaning import CleanData
    from data_ingestion import Session
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("CustomerBehaviour").getOrCreate()
    retail_data = Session().load_data(spark)
    customers_df = CleanData().clean_data(retail_data)
    transformed_df = TransformData().transform_data(customers_df)
    transformed_df.show()
