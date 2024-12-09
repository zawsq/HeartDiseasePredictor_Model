import pandas as pd
import numpy as np
from src.logger import logger


from sklearn.preprocessing import StandardScaler
def Feature_scaling(X_train_selected:pd.DataFrame ,X_test_selected:pd.DataFrame):
    """Performs standard scaling on the dataset fit on the xtrain only and then transform the x_test
    """
    logger.info("Starting feature scalign using standardization")
    
    try:
        feature_to_standardize = ['BMI','chronic_disease_score','health_days','lifestyle_score']

        #initiate standard scaler
        std_scaler = StandardScaler()

        X_train_selected[feature_to_standardize] = std_scaler.fit_transform(X_train_selected[feature_to_standardize])
        X_test_selected[feature_to_standardize] = std_scaler.transform(X_test_selected[feature_to_standardize])
        
        logger.info("Standardization was successful")
        
        return X_test_selected, X_test_selected
    
    except Exception as e:
        logger.info("an error has occured while doing standardization, {e}")

        