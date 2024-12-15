import joblib

def load_model(model_file_path: str):
    """
    Load the trained machine learning model from a file.

    Args:
        model_file_path (str): Path to the saved model file.

    Returns:
        object: The loaded model.
    """
    try:
        # Load the model using joblib
        model = joblib.load(model_file_path)
        return model
    except Exception as e:
        raise ValueError(f"Error loading model: {e}")