"""
This module contains the basic ETL (Extract, Transform, Load) operations for processing data in Python. It provides functions to extract data from various sources, transform it into a desired format, and load it into a target destination. The module is designed to be flexible and can be easily integrated into larger data processing pipelines.
Function Structure:
- extract_data(source): Extracts data from the specified source (e.g., CSV, JSON, database).
- transform_data(data): Transforms the extracted data into the desired format (e.g., cleaning, normalizing).
- load_data(data, destination): Loads the transformed data into the specified destination (e.g., database, file).
- main(): The main function that orchestrates the ETL process by calling the extract, transform, and load functions in sequence.

output:
proceessed_data: The final output after the ETL process, which can be used for further analysis or reporting.
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Rows in: 1200, dropped: 200, rows out: 1000")

class ETLProcessor:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def extract_data(self):
        """
        Extracts data from the specified sourc.
        return: DataFrame containing the extracted data
        """
        try:
            if self.source.endswith(".csv"):
                data = pd.read_csv(self.source)
            else:
                logging.error(f"Unsupported file format: {self.source.split('.')[-1]}")
            return data
        except Exception as e:
            logging.error(f"Error extracting data: {e}")
            
    
    def transform_data(self, data):
        """
        Transforms the extracteed data into the desireed format.
        params: data (DataFrame) - The extracted raw data to be transformed
        return: DataFrame containing the transformed data
        """
        try:
            # example: Handle null values & duplicates
            logging.info(f"Initial data shape: {data.shape[0]} rows, {data.shape[1]} columns")
            data = data.dropna()  # Drop rows with null values
            data = data.drop_duplicates()  # Drop duplicate rows
            logging.info(f"Final data shape: {data.shape[0]} rows, {data.shape[1]} columns")
            return data
        except Exception as e:
            logging.error(f"Error transforming data: {e}")

    def load_data(self, data):
        """
        Loads the transformed data into the specified destination.
        params: data (DataFrame) - The transformed data to be loaded
        """
        try:
            if self.destination.endswith(".csv"):
                data.to_csv(self.destination, index=False)
            else:
                logging.error(f"Unsupported file format: {self.destination.split('.')[-1]}")
            logging.info(f"Data successfully loaded to {self.destination}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")