import joblib

def load_model(model_file_path: str):
    """
    Load the trained machine learning model from a file which is saved
    in the model folder

    Args:
        model_file_path (str): Path to the saved model file

    Returns:
        object: The loaded model.
        
        sidenote: important thing that you load the saved model on what library you use
        to save it whether its joblib or pickle in this case its pickle
    """
    try:
        # Load the model using joblib
        model = joblib.load(model_file_path)
        return model
    except Exception as e:
        raise ValueError(f"Error loading model: {e}")