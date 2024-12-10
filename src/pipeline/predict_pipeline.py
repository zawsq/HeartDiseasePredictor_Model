#imports
from src.components.data_ingestion import load_data, clean_data
from src.components.data_transformation import (
    feature_encoding, mice_imputation, cleaning_imputation, 
    split_data, combine_datasets,
    handling_Inconsistencies, feature_engineering, feature_selection_with_rf
    )
from src.components.model_trainer import (
    feature_scaling, baseline_model, hyperparameter_tuning, evaluate_model, save_model 
    )

import pandas as pd
from src.logger import logger


def train_pipeline():
    """complete pipeline for loading, preprocessing the data and model training
    """
    try:
        # Load datasets
        df_1 = load_data('heart_2022_no_nans.csv')
        df_2 = load_data('heart_2022_with_nans.csv')
        
        # Clean datasets
        df_1 = clean_data(df_1)
        df_2 = clean_data(df_2)
        
        #performing feature encoding on datasets
        df_1 = feature_encoding(df_1)
        df_2 = feature_encoding(df_2)
        
        #imputing missing values on df_2 and splitting
        # X_train_imputed_df2, X_test_imputed_df2, y_train_df2, y_test_df2 = mice_imputation(
        #     df_2,"HeartDisease"
        # )
        
        #cleaning the imputation on df_2
        # X_train_imputed_df2 , X_test_imputed_df2 , y_train_df2 = cleaning_imputation(
        #     X_train_imputed_df2, X_test_imputed_df2, y_train_df2
        #     )
        
        #splitting df_1 then combining the two dataset
        print("About to call split_data function")
        X_train_df1, X_test_df1, y_train_df1, y_test_df1 = split_data(df_1, 'HeartDisease')
        
        X_train_df1 = X_train_df1[['HadAngina', 'HadStroke']]
        X_test_df1 = X_test_df1[['HadAngina', 'HadStroke']]
        
        print(y_train_df1.value_counts())
        print(X_test_df1)
        
        baseline_model(
            X_train_df1, y_train_df1,X_test_df1, y_test_df1
        )
        
        best_model = hyperparameter_tuning(
            X_train_df1,y_train_df1
        )
        
        evaluate_model(best_model, X_test_df1, y_test_df1)
        
        save_model(best_model, 'test2.pkl')
        
        print('Test was successful')
        raise ValueError
        #combining the two dataset
        X_train_combined, X_test_combined, y_train_combined, y_test_combined = combine_datasets(
            X_train_df1, X_test_df1,X_train_imputed_df2,X_test_imputed_df2,y_train_df1,
            y_test_df1,y_train_df2,y_test_df2
        )
        
        

        #feature engineering
        X_train_combined, X_test_combined = feature_engineering(
            X_train_combined, X_test_combined
        )
        
        #feature selection
        X_train_selected, X_test_selected, features = feature_selection_with_rf(
            X_train_combined,X_test_combined, y_train_combined
        )
        logger.info(f'Final feature check that was selected: {features}')
        #feature scaling
        X_train_selected, X_test_selected = feature_scaling(
            X_train_selected, X_test_selected
        )
        
        #Renaming the variables for clarity and consistency similar to how it was first split by train_test_split
        X_train, X_test , y_train , y_test = X_train_selected, X_test_selected , y_train_combined , y_test_combined
        
        #baseline model training
        baseline_model(
            X_train,y_train , X_test  , y_test
        )
        
        #hyperparameter tuning
        best_model = hyperparameter_tuning(
            X_train,y_train
        )
        
        #Evaluating the best model
        evaluate_model(best_model, X_test,y_test)
        
        #saving the best model for deployment and production
        save_model(best_model, "RandomForest_best_model.pkl")
        
    except Exception as e:
        logger.info(f"Train pipeline failed an error has occured {e}")
        
if __name__ == "__main__":
    #RUN
    train_pipeline()