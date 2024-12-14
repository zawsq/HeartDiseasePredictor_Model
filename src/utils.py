import os
import sys
from src.logger import logger



def set_project_root():
   PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
   if PROJECT_ROOT not in sys.path:  # Avoid adding the same path multiple times
        sys.path.append(PROJECT_ROOT)
  
    
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
        
        
import zipfile
def zip_model(file_name:str,zip_file_name:str ):
   '''
   file_name =    Path to your model file
   
   zip_file_name =     Output zip file name
   '''
   
   logger.info("starting to compress the pkl file to model folder")
   with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
      # Add file to the zip archive
      # Use arcname to exclude the "model/" prefix in the zip file if desired
      zipf.write(file_name, arcname="RandomForest_best_model.pkl")
      logger.info("The model was successfully compressed.")