
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
        file_path = os.path.join(os.getcwd(), 'data', 'raw', file_name)
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
    Perform a quick basic cleaning, including removing duplicates and renaming columns.

    Args:
        data (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    
    
    
    try:
        logger.info("Starting data cleaning process.")
        
        # Make a copy to ensure we're working with an independent DataFrame
        data = data.copy()
        
        # Drop duplicates
        data = data.drop_duplicates()
        logger.info("Duplicates removed.")

        # Rename the column 'HadHeartAttack' to 'HeartDisease'
        if 'HadHeartAttack' in data.columns:
            data = data.rename(columns={'HadHeartAttack': 'HeartDisease'})
            logger.info("Column 'HadHeartAttack' renamed to 'HeartDisease'.")
        else:
            logger.warning("Column 'HadHeartAttack' not found. No renaming performed.")
        
        return data
    except Exception as e:
        logger.exception("Error during data cleaning.")
        raise e
