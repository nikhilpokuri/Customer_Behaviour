### README.md

# Customer Behavior Analysis with PySpark

This project provides a detailed analysis of customer behavior using the Online Retail dataset. The project is structured into several modules, each responsible for different aspects of the data processing and analysis workflow using PySpark.

## Project Structure

```
my-pyspark-project/
|-data/
│  |- Online_Retail.csv  # Data file
|- src/
│   |- analysisNotebook.ipynb  # Jupyter notebook for analysis
│   |- data_ingestion.py  # Module for data loading
│   |- data_cleaning.py  # Module for data cleaning
│   |- data_transformation.py  # Module for data transformation
|- README.md  # Project documentation
|- requirements.txt  # List of Python dependencies
```

## Files and Modules

### 1. data_ingestion.py

This module is responsible for loading the data from the CSV file into a PySpark DataFrame.


### 2. data_cleaning.py

This module handles data cleaning tasks, such as filling missing values in specific columns.


### 3. data_transformation.py

This module includes transformation logic, such as formatting columns and converting data types.


### 4. analysisNotebook.ipynb

This Jupyter Notebook is used for exploratory data analysis and visualization. It ties together the data ingestion, cleaning, and transformation processes, and provides a space to explore the dataset interactively.


## Data

The dataset used in this project is the Online Retail dataset, which contains transactional data from an online retail store. The data includes fields like `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`, and `TotalPrice`.

## Open and run src/analysisNotebook.ipynb