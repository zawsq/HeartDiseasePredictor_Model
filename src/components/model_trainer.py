import pandas as pd
import numpy as np
from src.logger import logger



"""Feature Scaling using Standardization"""
#importing used library in the function
from sklearn.preprocessing import StandardScaler
def feature_scaling(X_train_selected:pd.DataFrame ,X_test_selected:pd.DataFrame):
    """Performs standard scaling on the dataset fit on the xtrain only and then transform the x_test
    """
    logger.info("Starting feature scaling using standardization")
    
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
        
      
        
"""baseline model"""
#importing our models and evaluation metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score, recall_score, precision_score, accuracy_score
def baseline_model(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series):
    """Train the baseline Random Forest model and return performance metrics."""
    
    try:
       
        
        # Initializing Random Forest
        rf_model = RandomForestClassifier(random_state=42)
        
        # Training the model
        logger.info("start fitting the random forest")
        rf_model.fit(X_train, y_train)
        logger.info("successfully fitted random forest")
        
        # Making predictions on the test set
        y_pred = rf_model.predict(X_test)
        
        # Evaluating the model
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:, 1])

        # Log the metrics
        logger.info("Random Forest Model Baseline Evaluation:")
        logger.info(f" - Accuracy: {accuracy}")
        logger.info(f" - F1 Score: {f1}")
        logger.info(f" - Recall: {recall}")
        logger.info(f" - Precision: {precision}")
        logger.info(f" - ROC AUC: {roc_auc}")

    except Exception as e:
        logger.error(f"An error occurred during model evaluation: {e}")
    
    return rf_model





"""Hyper parameter tuning """
#importing libraries to be used
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer
from scipy.stats import randint


def hyperparameter_tuning(X_train: pd.DataFrame, y_train: pd.Series):
    """Performs hyperparameter tuning on RandomForest using RandomizedSearchCV."""
    
    try:
        #hyperparameter search space
        param_distributions = { 
            'n_estimators': randint(700, 1000),
            'max_depth': randint(3, 30),
            'min_samples_split': randint(2, 20),
            'min_samples_leaf': randint(1, 20),
            'class_weight': ['balanced', {0: 1, 1: 5.5}, {0: 1, 1: 6},{0: 1, 1: 6.25},{0: 1, 1: 6.5},{0: 1, 1: 6.75}],
        }
        
        # Initialize RandomForestClassifier
        rf_model = RandomForestClassifier(random_state=42)
        
        # StratifiedKFold cross-validation (5 folds)
        cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
        
        # Define the scorer for RandomizedSearchCV
        f1_scorer = make_scorer(f1_score)

        # Initialize RandomizedSearchCV
        random_search = RandomizedSearchCV(
            estimator=rf_model,
            param_distributions=param_distributions,
            scoring=f1_scorer,
            n_iter=50,  # Number of random search iterations
            cv=cv,
            verbose=1,
            random_state=42,
            n_jobs=7  
        )
        
        # Fit the model with the random search
        logger.info("Starting hyperparameter tuning...")
        random_search.fit(X_train, y_train)
        logger.info("Hyperparameter tuning completed.")
        
        # Log the best hyperparameters and score
        best_model = random_search.best_estimator_
        logger.info(f"Best Hyperparameters: {random_search.best_params_}")
        logger.info(f"Best F1 Score: {random_search.best_score_}")
        
        return best_model

    except Exception as e:
        logger.error(f"An error occurred during hyperparameter tuning: {e}")
        return None
    
    
    
"""FINAL EVALUATION OF MODEL AFTER HYPERPARAMETER TUNING"""    
def evaluate_model(best_model, X_test: pd.DataFrame, y_test: pd.Series):
    """Evaluates the model using multiple metrics: Accuracy, F1, ROC AUC, Recall, Precision."""
    
    try:
        # Make predictions on the test set
        y_pred = best_model.predict(X_test)
        y_pred_proba = best_model.predict_proba(X_test)[:, 1]  # Probabilities for ROC AUC
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        
        # Log the evaluation results
        logger.info("Final Model Evaluation:")
        logger.info(f"Accuracy: {accuracy:.4f}")
        logger.info(f"F1 Score: {f1:.4f}")
        logger.info(f"ROC AUC Score: {roc_auc:.4f}")
        logger.info(f"Recall: {recall:.4f}")
        logger.info(f"Precision: {precision:.4f}")
        
        return {
            'accuracy': accuracy,
            'f1_score': f1,
            'roc_auc': roc_auc,
            'recall': recall,
            'precision': precision
        }
    
    except Exception as e:
        logger.error(f"An error occurred during model evaluation: {e}")
        return None
    
    
    
"""SAVING OUR FINAL BEST MODEL FOR DEPLOYMENT"""    
#libraries for saving our model    
import joblib
import os    
def save_model(model, model_filename: str):
    """Saves the trained model to a file in the 'model' directory using joblib."""
    try:
        # Define the correct model directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.join(current_dir, '..', '..')  # Navigate 2 lvls up components>src>root
        model_dir = os.path.join(project_root, 'model')  # Use the 'model' folder
        
        # Create the model directory if it doesn't exist
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        
        # Full path to save the model
        model_path = os.path.join(model_dir, model_filename)
        
        # Save the model
        joblib.dump(model, model_path)
        logger.info(f"Model saved to {model_path}")
    except Exception as e:
        logger.error(f"An error occurred while saving the model: {e}")