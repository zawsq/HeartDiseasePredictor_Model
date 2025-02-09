import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib  # For loading the pre-trained model
from src.prediction_utils import (
    calculate_lifestyle_score,
    calculate_chronic_disease_score,
    calculate_bmi,
    calculate_health_days,
    map_age
)
from deployment.Api.model_loader import load_model
import logging as logger


def preprocess_user_input(user_input:dict):
    """
    Preprocesses the user input from the web form into a pandas DataFrame
    and applies necessary transformations to match the model's expected input order.
    
    Parameters:
    - user_input (dict): User input values from the web form.
    
    Returns:
    - np.ndarray: Processed data ready for model prediction (standardized).
    """
    # Log the incoming user input
    logger.info("Received user input for preprocessing: %s", user_input)

    # Check for missing required fields
    required_fields = ['Age', 'Height', 'Weight','PhysicalHealthDays' , 'ECigaretteUsage', 'AlcoholDrinker', 'PhysicalActivities',
                       'RemovedTeeth', 'SleepHours', 'HadStroke', 'HadCOPD', 'HadDiabetes', 'HadArthritis', 'HadKidneyDisease', 
                       'HadSkinCancer', 'HadAsthma','SmokerStatus' , 'MentalHealthDays']
    
    for field in required_fields:
        if field not in user_input:
            logger.error("Missing required field: %s", field)
            raise ValueError(f"Missing required field: {field}")
    
    # Convert user input into a DataFrame
    user_df = pd.DataFrame([user_input])
    logger.info("Converted user input into DataFrame: %s", user_df.head())

    # Calculate lifestyle score
    lifestyle_score = calculate_lifestyle_score(
        user_input['SmokerStatus'],
        user_input['ECigaretteUsage'],
        user_input['AlcoholDrinker'],
        user_input['PhysicalActivities'],
        user_input['RemovedTeeth'],
        user_input['SleepHours']
    )
    user_df['lifestyle_score'] = lifestyle_score
    logger.info("Calculated lifestyle score: %s", lifestyle_score)

    # Calculate chronic disease score
    chronic_disease_score = calculate_chronic_disease_score(
        user_input['HadStroke'],
        user_input['HadCOPD'],
        user_input['HadDiabetes'],
        user_input['HadArthritis'],
        user_input['HadKidneyDisease'],
        user_input['HadSkinCancer'],
        user_input['HadAsthma']
    )
    user_df['chronic_disease_score'] = chronic_disease_score
    logger.info("Calculated chronic disease score: %s", chronic_disease_score)

    # Calculate BMI
    bmi = calculate_bmi(user_input['Weight'], user_input['Height'])
    user_df['BMI'] = bmi
    logger.info("Calculated BMI: %s", bmi)

    # Calculate health days (sum of physical and mental health days)
    health_days = calculate_health_days(user_input['PhysicalHealthDays'], user_input['MentalHealthDays'])
    user_df['health_days'] = health_days
    logger.info("Calculated health days: %s", health_days)

    #Add 'AgeCategory' by calling the map_age_to_category function
    age = user_input['Age']
    user_df['AgeCategory'] = map_age(age)
    logger.info("Mapped age to category: %s", user_df['AgeCategory'])



    # Define the correct column order
    column_order = [
        'HadAngina', 'AgeCategory', 'BMI', 'chronic_disease_score', 'health_days', 'lifestyle_score'
    ]
    
    # Reorder the columns to match the training order
    user_df = user_df[column_order]
    logger.info("Reordered columns for model input: %s", user_df.head())

    
    columns_to_scale = ['BMI', 'chronic_disease_score', 'health_days', 'lifestyle_score']

    try:
        # Load the scaler that was saved from the notebook
        scaler = joblib.load('model/scaler.pkl')  
        logger.info("Scaler loaded successfully.")
        
        # Scale only the specified columns
        user_df_scaled = user_df.copy()  # Create a copy of the original DataFrame
        user_df_scaled[columns_to_scale] = scaler.transform(user_df[columns_to_scale])
        logger.info("Specified columns successfully standardized.")
        
    except KeyError as ke:
        logger.error("One or more columns to scale are missing in the input data: %s", str(ke))
        raise ValueError(f"Missing columns for scaling: {ke}")
    except Exception as e:
        logger.error("Error loading scaler or transforming data: %s", str(e))
        raise ValueError(f"Error loading scaler or transforming data: {e}")

    return user_df_scaled

def predict(user_input: pd.DataFrame):
    """
    Predict the likelihood of heart disease based on user input.

    Parameters:
    - user_input dataframe now because it was transformed in the preprocess function
    
    
    Returns:
    - prediction: The prediction result from the model and gets sent to the api.
    """
    # Preprocess the user input (calculate scores and transform data)
    logger.info("Preprocessing user input for prediction.")
    processed_data = preprocess_user_input(user_input)
    
    # Load the model (this can be done once and cached in production for performance)
    try:
        model = load_model('model/RandomForest_best_model.pkl')
        logger.info("Model loaded successfully.")
    except Exception as e:
        logger.error("Error loading model: %s", str(e))
        raise ValueError(f"Error loading model: {e}")
   
    # Make the prediction
    prediction = model.predict(processed_data)
    logger.info("Model prediction: %s", prediction)

    return prediction
    
