import pandas as pd
import numpy as np
import os


from src.logger import logger


'''FEATURE ENCODING THE DATASET'''

def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Dropping unnecessary columns...")
    columns_to_drop = ['HeightInMeters', 'WeightInKilograms', 'State', 'RaceEthnicityCategory']
    try:
        df.drop(columns=columns_to_drop, inplace=True)
    except Exception as e:
        logger.warning(f"Some columns may already have been dropped: {e}")
    return df

def encode_general_health(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for GeneralHealth column...")
    gen_health_map = {
        'Poor': 1,
        'Fair': 2,
        'Good': 3,
        'Very good': 4,
        'Excellent': 5,
    }
    if df['GeneralHealth'] in df.columns:
        df['GeneralHealth'] = df['GeneralHealth'].map(gen_health_map)
        logger.info("Encoding for GeneralHealth completed.")
    else:
        logger
    return df

def encode_last_checkup(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for LastCheckupTime column...")
    last_checkup_mapping = {
        'Within past year (anytime less than 12 months ago)': 0,
        'Within past 2 years (1 year but less than 2 years ago)': 1,
        'Within past 5 years (2 years but less than 5 years ago)': 2,
        '5 or more years ago': 3,
    }
    if 'LastCheckupTime' in df.columns:
        df['LastCheckupTime'] = df['LastCheckupTime'].map(last_checkup_mapping)
        logger.info("Encoding for LastCheckupTime completed.")
    else:
        logger.warning("'LastCheckupTime' column not found in the dataset.")
    return df

def encode_age_category(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for AgeCategory column...")
    age_mapping = {
        'Age 18 to 24': 1,
        'Age 25 to 29': 2,
        'Age 30 to 34': 3,
        'Age 35 to 39': 4,
        'Age 40 to 44': 5,
        'Age 45 to 49': 6,
        'Age 50 to 54': 7,
        'Age 55 to 59': 8,
        'Age 60 to 64': 9,
        'Age 65 to 69': 10,
        'Age 70 to 74': 11,
        'Age 75 to 79': 12,
        'Age 80 or older': 13
    }
    if 'AgeCategory' in df.columns:
        if not pd.api.types.is_numeric_dtype(df['AgeCategory']):
            df['AgeCategory'] = df['AgeCategory'].map(age_mapping)
            logger.info("Encoding for AgeCategory completed.")
        else:
            logger.info("'AgeCategory' column is already numeric.")
    else:
        logger.warning("'AgeCategory' column not found in the dataset.")
    return df


def encode_had_diabetes(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for HadDiabetes column...")
    had_diabetes_mapping = {
        'Yes': 2,
        'No': 0,
        'No, pre-diabetes or borderline diabetes': 1,
        'Yes, but only during pregnancy (female)': 1,
    }
    if 'HadDiabetes' in df.columns:
        df['HadDiabetes'] = df['HadDiabetes'].map(had_diabetes_mapping)
        logger.info("Encoding for HadDiabetes completed.")
    else:
        logger.warning("'HadDiabetes' column not found in the dataset.")
    return df


def encode_removed_teeth(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for RemovedTeeth column...")
    removed_teeth_mapping = {
        'None of them': 0,
        '1 to 5': 1,
        '6 or more, but not all': 2,
        'All': 3,
    }
    if 'RemovedTeeth' in df.columns:
        df['RemovedTeeth'] = df['RemovedTeeth'].map(removed_teeth_mapping)
        logger.info("Encoding for RemovedTeeth completed.")
    else:
        logger.warning("'RemovedTeeth' column not found in the dataset.")
    return df


def encode_smoker_status(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for SmokerStatus column...")
    smoker_status_mapping = {
        'Never smoked': 0,
        'Former smoker': 1,
        'Current smoker - now smokes some days': 2,
        'Current smoker - now smokes every day': 3
    }
    if 'SmokerStatus' in df.columns:
        df['SmokerStatus'] = df['SmokerStatus'].map(smoker_status_mapping)
        logger.info("Encoding for SmokerStatus completed.")
    else:
        logger.warning("'SmokerStatus' column not found in the dataset.")
    return df


def encode_e_cigarette_usage(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for ECigaretteUsage column...")
    e_cigarette_usage_mapping = {
        'Not at all (right now)': 0,
        'Never used e-cigarettes in my entire life': 1,
        'Use them some days': 2,
        'Use them every day': 3,
    }
    if 'ECigaretteUsage' in df.columns:
        df['ECigaretteUsage'] = df['ECigaretteUsage'].map(e_cigarette_usage_mapping)
        logger.info("Encoding for ECigaretteUsage completed.")
    else:
        logger.warning("'ECigaretteUsage' column not found in the dataset.")
    return df


def encode_covid_pos(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for CovidPos column...")
    covid_pos_mapping = {
        'No': 0,
        'Tested positive using home test without a health professional': 1,
        'Yes': 2,
    }
    if 'CovidPos' in df.columns:
        if not pd.api.types.is_numeric_dtype(df['CovidPos']):
            df['CovidPos'] = df['CovidPos'].map(covid_pos_mapping)
            logger.info("Encoding for CovidPos completed.")
        else:
            logger.info("'CovidPos' column is already numeric. Skipping encoding.")
    else:
        logger.warning("'CovidPos' column not found in the dataset.")
    return df

def encode_tetanus_last_10(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting encoding for TetanusLast10Tdap column...")
    tetanus_last_10_mapping = {
        'Yes, received tetanus shot but not sure what type': 0,
        'No, did not receive any tetanus shot in the past 10 years': 1,
        'Yes, received Tdap': 2,
        'Yes, received tetanus shot, but not Tdap': 3
    }
    if df['TetanusLast10Tdap'] in df.columns:
        
        df['TetanusLast10Tdap'] = df['TetanusLast10Tdap'].map(tetanus_last_10_mapping)
        logger.info("Encoding for TetanusLast10Tdap completed.")
    else:
        logger.info("Encoding for TetanusLast10dap failed")
    return df

# One hot encoding for Sex
def encode_sex(df: pd.DataFrame) -> pd.DataFrame:
    '''encoding feature "Sex" '''
    logger.info("Starting one-hot encoding for Sex column...")
    if df['sex'] in df.columns:
        df = pd.get_dummies(df, columns=['Sex'], prefix='', prefix_sep='')
        logger.info("One-hot encoding for Sex feature completed.")
    else:
        logger.info("One-hot encoding for Sex feature failed")
    return df

# Master transformation function
def feature_encoding(df: pd.DataFrame) -> pd.DataFrame:
    df = encode_general_health(df)
    df = drop_columns(df)
    df = encode_last_checkup(df)
    df = encode_age_category(df)
    df = encode_had_diabetes(df)
    df = encode_removed_teeth(df)
    df = encode_smoker_status(df)
    df = encode_e_cigarette_usage(df)
    df = encode_covid_pos(df)
    df = encode_tetanus_last_10(df)
    df = encode_sex(df)
    df = encode_health_conditions(df)
    logger.info("feature encoding completed.")
    return df


def encode_health_conditions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps binary health condition features from 'Yes'/'No' to 1/0 using a predefined mapping.
    'healt_conditions_mapping' 
    
    Args:
        df (pd.DataFrame): The DataFrame containing health condition features.

    Returns:
        pd.DataFrame: The transformed DataFrame with the mapped values.
    """
    logger.info("Starting transformation of health condition features.")
    
    
    
    health_conditions_mapping = {
     'Yes': 1,
     'No': 0,
    
    }

    
    # List of columns to apply the mapping
    health_condition_columns = [
        'PhysicalActivities', 'HeartDisease', 'HadAngina', 'HadStroke', 'HadAsthma',
        'HadSkinCancer', 'HadCOPD', 'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis',
        'ChestScan', 'DeafOrHardOfHearing', 'BlindOrVisionDifficulty', 'DifficultyConcentrating',
        'DifficultyWalking', 'DifficultyDressingBathing', 'DifficultyErrands', 'AlcoholDrinkers',
        'HIVTesting', 'FluVaxLast12', 'HighRiskLastYear', 'PneumoVaxEver'
    ]
    
    # Ensure all specified columns are present in the DataFrame if missing gets logged and checked
    missing_columns = [col for col in health_condition_columns if col not in df.columns]
    if missing_columns:
        logger.warning(f"The following columns are missing and will be skipped: {missing_columns}")
    
    # Apply the mapping to the respective columns
    for column in health_condition_columns:
        if column in df.columns:
            logger.info(f"Transforming column: {column}")
            df[column] = df[column].map(health_conditions_mapping)
        else:
            logger.warning(f"Skipping column '{column}' as it is not present in the DataFrame.")
    
    
    logger.info("Transformation of health condition features completed.")
    return df


"""IMPUTING THE MISSING VALUES IN DF USING MICE IMPUTATIONG"""

#importing libraries that we will use 
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def mice_imputation(df: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42) -> tuple:
    """
    Function to perform MICE imputation on a DataFrame after splitting it into train and test sets.
    
    Args:
    df (pd.DataFrame): DataFrame containing the data.
    target_column (str): The column name to be used as the target variable (y).
    test_size (float): Proportion of the dataset to be used as test data.
    random_state (int): Random state for reproducibility.
    
    Returns:
    tuple: The transformed X_train_df2, X_test_df2, y_train_df2, y_test_df2 DataFrames.
    """
    
    # Log the start of the transformation
    logger.info(f"Starting MICE imputation for target: {target_column}...")
    
    # Exclude the target column and any specified columns
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split the data into training and testing sets
    X_train_df2, X_test_df2, y_train_df2, y_test_df2 = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Initialize the MICE imputer
    mice_imputer = IterativeImputer(max_iter=50, random_state=random_state)
    
    # Apply the imputer to the training data
    X_train_imputed_df2 = pd.DataFrame(
        mice_imputer.fit_transform(X_train_df2), columns=X_train_df2.columns
    )
    
    # Apply the same imputer to the test data
    X_test_imputed_df2 = pd.DataFrame(
        mice_imputer.transform(X_test_df2), columns=X_test_df2.columns
    )
    
    # Log completion of the transformation
    logger.info("MICE imputation completed successfully.")
    
    # Return the transformed data
    return X_train_imputed_df2, X_test_imputed_df2, y_train_df2, y_test_df2


def Cleaning_imputation(X_train_imputed, X_test_imputed):
    
    '''
    performing mice imputation results with the imputed values mostly having alot of float values
    that might be inconsistent and such we will be cleaning them
    '''
    # Round off the MICE imputation results before clipping
    X_train_imputed = X_train_imputed.round().astype(int)
    X_test_imputed = X_test_imputed.round().astype(int)
    
    # Clip values within the specified ranges
    X_train_imputed['MentalHealthDays'] = X_train_imputed['MentalHealthDays'].clip(0, 30)
    X_test_imputed['MentalHealthDays'] = X_test_imputed['MentalHealthDays'].clip(0, 30)

    # Clip other features similarly
    X_train_imputed['PhysicalHealthDays'] = X_train_imputed['PhysicalHealthDays'].clip(0, 30)
    X_test_imputed['PhysicalHealthDays'] = X_test_imputed['PhysicalHealthDays'].clip(0, 30)

    # Clip AgeCategory
    X_train_imputed['AgeCategory'] = X_train_imputed['AgeCategory'].clip(lower=1, upper=13)
    X_test_imputed['AgeCategory'] = X_test_imputed['AgeCategory'].clip(lower=1, upper=13)

    # Remove any GeneralHealth values equal to 0 in the training set
    mask = X_train_imputed['GeneralHealth'] != 0
    X_train_imputed = X_train_imputed[mask]
    y_train_imputed = y_train_imputed[mask]  # Adjust y_train accordingly if you filter X_train to be the same number of rows

    return X_train_imputed, X_test_imputed
    
 
'''COMBINING THE DATASET ''' 
    
    
    
def split_data(df1, target_column='HeartDisease', test_size=0.2, random_state=42):
    """
    This function splits df1 into training and testing sets, ensuring stratification of the target variable.
    this is so that we match the df2 and we can combine them 
    
    Parameters:
    - df1: pandas DataFrame containing the dataset to be split.
    - target_column: str, the name of the target variable column (default is 'HeartDisease').
    - test_size: float, the proportion of the dataset to include in the test split (default is 0.2).
    - random_state: int, random seed for reproducibility (default is 42).
    
    Returns:
    - X_train_df1: Features for the training set.
    - X_test_df1: Features for the testing set.
    - y_train_df1: Target variable for the training set.
    - y_test_df1: Target variable for the testing set.
    """
    try:
        # Separate the features (X) and target variable (y)
        X_df1 = df1.drop(columns=[target_column])  # Drop the target column to get features
        y_df1 = df1[target_column]  # The target column

        # Split the data into training and testing sets with stratification on the target variable
        X_train_df1, X_test_df1, y_train_df1, y_test_df1 = train_test_split(
            X_df1, y_df1, test_size=test_size, random_state=random_state, stratify=y_df1
        )

        # Log the split data information
        logger.info(f"Data split completed. X_train_df1 and X_test_df1 are ready with test size: {test_size}.")
        
        return X_train_df1, X_test_df1, y_train_df1, y_test_df1

    except Exception as e:
        logger.error(f"Error occurred during data splitting: {e}")
        raise    
    
def combine_datasets(X_train_df1, X_test_df1, X_train_df2, X_test_df2, y_train_df1, y_test_df1, y_train_df2, y_test_df2):
    """
    Combines two datasets (df1 and df2) into a single dataset
    
    Args:
    X_train_df1, X_test_df1, y_train_df1, y_test_df1: DataFrames for the first dataset (df1).
    X_train_df2, X_test_df2, y_train_df2, y_test_df2: DataFrames for the second dataset (df2) after MICE imputation.
    
    Returns:
    Combined X_train, X_test, y_train, y_test DataFrames.
    """
    # Combine the training features and target variables
    X_train_combined = pd.concat([X_train_df1, X_train_df2], axis=0)
    X_test_combined = pd.concat([X_test_df1, X_test_df2], axis=0)
    
    # Combine the target variables
    y_train_combined = pd.concat([y_train_df1, y_train_df2], axis=0)
    y_test_combined = pd.concat([y_test_df1, y_test_df2], axis=0)
    
    return X_train_combined, X_test_combined, y_train_combined, y_test_combined


"""Handling inconsistent values
"""
def Handling_Inconsistencies(row):
    '''Check for high Physical and Mental Health scores, and classify based on chronic conditions.
    there are some inconsistent values like having physical health days of 30 (meaning they are experiencing
    physical health problems everyday) but their general health score is == 'Excellent' which doesnt match
    up thus we will use this function to fix these along with other inconsistencies 
    '''
    try:
        if row['PhysicalHealthDays'] >= 25 or row['MentalHealthDays'] >= 25:
            return 1  # 'Poor' health classification
        
        chronic_conditions = [
            row['HadAsthma'],
            row['HadSkinCancer'],
            row['HadCOPD'],
            row['HadDepressiveDisorder'],
            row['HadKidneyDisease'],
            row['HadArthritis'],
            row['HadDiabetes'],
            row['HadAngina'],
            row['HadStroke'],
        ]
        
        # Count how many chronic conditions are present
        conditions_count = sum(chronic_conditions)

        if conditions_count >= 3:  # Three or more conditions
            return 0  # 'Poor'
        elif conditions_count == 2:  # Two conditions
            return 1  # 'Fair'
        elif conditions_count == 1:  # One condition
            return 2  # 'Good'

        # If the existing GenHealth value is 'Poor', don't classify it as 'Good'
        existing_genhealth = row['GeneralHealth']
        if existing_genhealth == 1:  # If 'Poor' is present
            return 1  # Keep as 'Poor'

        return existing_genhealth  # Default: return existing GenHealth value

    except Exception as e:
        logger.error(f"Error in determining GenHealth: {e}")
        return None  # Return None if an error occurs



def transform_and_apply_genhealth(X_train_combined, X_test_combined):
    """applying tranformation handling inconsistencies 
    """
    try:
        # Log the start of the transformation
        logger.info("Starting GeneralHealth transformation...")

        # Apply the determine_genhealth function to both train and test data
        X_train_combined['GeneralHealth'] = X_train_combined.apply(Handling_Inconsistencies, axis=1)
        X_test_combined['GeneralHealth'] = X_test_combined.apply(Handling_Inconsistencies, axis=1)

        # Log successful transformation
        logger.info("GeneralHealth transformation completed successfully.")
        
        return X_train_combined, X_test_combined
    except Exception as e:
        logger.error(f"Error in transforming GeneralHealth: {e}")
        raise  # Re-raise exception to be handled upstream

"""FEATURE ENGINEERING"""

def calculate_lifestyle_score(row: pd.Series) -> float:
    '''
    Calculate the lifestyle score based on various health behaviors and conditions.
    
    Parameters:
    - row (pd.Series): A single row from the DataFrame (each row contains a set of feature values for a sample).
    
    Returns:
    - score (float): A lifestyle score for the given row, indicating overall lifestyle health.
    '''
    try:
        score = 0
        
        # Smoker Status
        if row['SmokerStatus'] == 3:  # Current smoker - now smokes every day
            score -= 1
        elif row['SmokerStatus'] == 2:  # Current smoker - smokes some days
            score -= 0.5
        elif row['SmokerStatus'] == 1:  # Former smoker
            score += 0  # Neutral for former smokers
        elif row['SmokerStatus'] == 0:  # Never smoked
            score += 1

        # E-Cigarette Usage (Vaping)
        if row['ECigaretteUsage'] == 3:  # Use e-cigarettes every day
            score -= 1
        elif row['ECigaretteUsage'] == 2:  # Use e-cigarettes some days
            score -= 0.5
        elif row['ECigaretteUsage'] == 1:  # Never used e-cigarettes in my entire life
            score += 0  # Neutral for non-users
        elif row['ECigaretteUsage'] == 0:  # Not at all (right now)
            score += 1

        # Alcohol Drinkers
        if row['AlcoholDrinkers'] == 1:  # Alcohol drinker
            score -= 1
        elif row['AlcoholDrinkers'] == 0:  # Non-alcohol drinker
            score += 1

        # Physical Activity
        if row['PhysicalActivities'] == 0:  # No physical activity
            score -= 1
        elif row['PhysicalActivities'] == 1:  # Any physical activity
            score += 1

        # Removed Teeth
        if row['RemovedTeeth'] == 0:  # No teeth removed
            score += 1
        elif 1 <= row['RemovedTeeth'] <= 1:  # 1 to 5 teeth removed
            score += 0  # Neutral
        elif 2 <= row['RemovedTeeth'] <= 2:  # 6 or more, but not all teeth removed
            score -= 0.5
        elif row['RemovedTeeth'] == 3:  # All teeth removed
            score -= 1

        # Sleep Hours
        if row['SleepHours'] < 6:  # Less than 6 hours of sleep
            score -= 1
        elif row['SleepHours'] > 10:  # More than 10 hours of sleep
            score -= 1
        elif 7 <= row['SleepHours'] <= 9:  # Optimal sleep (7-9 hours)
            score += 1
        else:  # Between 6 and 7, or between 9 and 10 hours of sleep
            score += 0  # Neutral

        return score

    except Exception as e:
        logger.error(f"Error calculating lifestyle score: {e}")
        raise  # Re-raise the exception for the pipeline to handle

def feature_engineering(X_combined: pd.DataFrame) -> pd.DataFrame:
    '''
    Perform feature engineering for the given dataset X_combined.
    
    Parameters:
    - X_combined (pd.DataFrame): The combined dataset containing the features.
    
    Returns:
    - X_combined (pd.DataFrame): The dataset with new features created and selected features dropped.
    '''
    try:
        logger.info("Starting feature engineering...")

        # Create Chronic Disease Score (multiplicative)
        X_combined['chronic_disease_score'] = (
            (X_combined['HadStroke'] + 1) * (X_combined['HadCOPD'] + 1) * (X_combined['HadDiabetes'] + 1)
            * (X_combined['HadArthritis'] + 1) * (X_combined['HadKidneyDisease'] + 1) * (X_combined['HadSkinCancer'] + 1) * (X_combined['HadAsthma'] + 1)
        )
        logger.info("Chronic disease score created.")

        # Create health days (additive)
        X_combined['health_days'] = X_combined['PhysicalHealthDays'] + X_combined['MentalHealthDays']
        logger.info("Health days feature created.")
        
        # Calculate lifestyle score
        X_combined['lifestyle_score'] = X_combined.apply(calculate_lifestyle_score, axis=1)
        logger.info("Lifestyle score feature created.")
        
        # Drop used features to avoid multicollinearity
        features_to_drop = [
            'HadStroke', 'HadCOPD', 'HadDiabetes', 'HadArthritis', 'PhysicalHealthDays', 'MentalHealthDays',
            'ECigaretteUsage', 'SmokerStatus', 'AlcoholDrinkers', 'PhysicalActivities', 'MentalHealthDays', 
            'SleepHours', 'HadAsthma', 'HadSkinCancer', 'HadKidneyDisease', 'RemovedTeeth', 'HighRiskLastYear',
            'TetanusLast10Tdap'
        ]
        X_combined.drop(features_to_drop, axis=1, inplace=True)
        logger.info(f"Dropped features: {features_to_drop}")

        return X_combined

    except Exception as e:
        logger.error(f"Error during feature engineering: {e}")
        raise  


def transform_and_select_features(X_train_combined: pd.DataFrame, X_test_combined: pd.DataFrame) -> pd.DataFrame:
    '''
    Apply feature engineering / interactions to both training and test datasets.
    
    Parameters:
    - X_train_combined (pd.DataFrame): Training dataset.
    - X_test_combined (pd.DataFrame): Test dataset.
    
    Returns:
    - X_train_combined (pd.DataFrame): Transformed training dataset with engineered features.
    - X_test_combined (pd.DataFrame): Transformed test dataset with engineered features.
    '''
    try:
        logger.info("Starting data transformation...")

        # Apply feature engineering to both training and test data
        X_train_combined = feature_engineering(X_train_combined)
        X_test_combined = feature_engineering(X_test_combined)
        
        logger.info("Feature engineering applied successfully.")
        
        return X_train_combined, X_test_combined

    except Exception as e:
        logger.error(f"Error during data transformation in pipeline: {e}")
        raise  
    
"""FEATURE SELECTION """    

#importing libraries that we will be using to clarify which are used
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import make_scorer, f1_score

def feature_selection_with_rf(X_train_combined, X_test_combined, y_train_combined):
    """
    Performs feature selection using Random Forest and cross-validation.
    
    Args:
    X_train_combined, X_test_combined: DataFrames for training and test features.
    y_train_combined: Series for target variable in the training data.
    
    Returns:
    X_train_selected, X_test_selected: DataFrames with selected features.
    """
    try:
        logger.info("Initializing Random Forest model for feature selection.")
        
        # Initialize and fit Random Forest model
        rf_model = RandomForestClassifier(random_state=42)
        rf_model.fit(X_train_combined, y_train_combined)
        logger.info("Random Forest model fitted.")
        
        # Feature selection based on feature importance
        selector = SelectFromModel(rf_model, prefit=True)
        logger.info("Feature selection completed using Random Forest model.")

        # Transform training and test sets to include only selected features
        X_train_selected = selector.transform(X_train_combined)
        X_test_selected = selector.transform(X_test_combined)

        # Convert selected features back to DataFrame for clarity
        selected_features = X_train_combined.columns[selector.get_support()]
        X_train_selected = pd.DataFrame(X_train_selected, columns=selected_features)
        X_test_selected = pd.DataFrame(X_test_selected, columns=selected_features)
        logger.info(f"Selected features: {selected_features}")

        # Initialize Stratified K-Folds for cross-validation
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        f1_scorer = make_scorer(f1_score)

        # Perform cross-validation with selected features
        logger.info("Performing cross-validation with selected features.")
        f1_scores = cross_val_score(rf_model, X_train_selected, y_train_combined, cv=cv, scoring=f1_scorer)

        # Output cross-validation F1 scores
        logger.info(f"F1 Cross-validated scores with selected features: {f1_scores}")
        logger.info(f"Mean F1 score with selected features: {f1_scores.mean()}")

        # Display shape of the transformed data
        logger.info(f"Shape of selected data: {X_train_selected.shape}")
        
        return X_train_selected, X_test_selected, selected_features
    
    except Exception as e:
        logger.error(f"Error during feature selection process: {e}")
        raise





