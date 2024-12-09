
import os
import sys
#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
#sys.path.append(PROJECT_ROOT)
#sys.path.append("C:\\Users\\exis\\python files exis\\projects\\proffesional projects\\Heart Disease Predictor Model")

import pandas as pd
from src.logger import logger

def load_data(file_name: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.
    """
    try:
        # Define the file path
        file_path = os.path.join(os.getcwd(), 'notebook', 'data', 'raw', file_name)
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"The file {file_name} was not found at {file_path}")
        
        # Load the data
        logger.info(f"Loading data from {file_path}")
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully with shape {data.shape}")
        return data
    except Exception as e:
        logger.exception(f"Error loading data: {e}")
        raise e

        
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Perform a quick basic cleaning removing duplicates in the data
    """
    try:
        logger.info("Starting data cleaning process.")
        
        # Drop duplicates
        data = data.drop_duplicates()
        logger.info("Duplicates removed.")
        
        return data
    except Exception as e:
        logger.exception(f"Error during data cleaning: {e}")
        raise e
    
    
if __name__ == "__main__":
    try:
        # Load datasets
        df_1 = load_data('heart_2022_no_nans.csv')
        df_2 = load_data('heart_2022_with_nans.csv')
        print(f"Data 1 Shape: {df_1.shape}, Data 2 Shape: {df_2.shape}")
        
        # Clean datasets
        df_1 = clean_data(df_1)
        df_2 = clean_data(df_2)
        
        logger.info("Data processed successfully.")
        print(f"Data 1 Shape: {df_1.shape}, Data 2 Shape: {df_2.shape}")
    except Exception as e:
        logger.exception(f"Error in main pipeline: {e}")
        print(f"Error in pipeline: {e}")