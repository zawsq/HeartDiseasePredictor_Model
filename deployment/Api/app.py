from fastapi import FastAPI
from schema import HeartDiseaseInput  # Ensure correct import
from src.pipeline.predict_pipeline import predict
from src.logger import logger
import uvicorn


app = FastAPI()

@app.post('/predict')
def predict_endpoint(user_input: HeartDiseaseInput):
    """
    Endpoint for predicting heart disease based on user input.
    
    Parameters:
    - user_input (HeartDiseaseInput): User input data from the web form.
    
    Returns:
    - dict: The prediction result.
    """
    
    # Log the incoming request
    logger.info("Received prediction request with input: %s", user_input.model_dump())

    try:
        # Convert user input to dictionary using Pydantic's .model_dump() method
        user_input_dict = user_input.model_dump()

        # Log the input dictionary before prediction
        logger.info("Converted user input to dictionary: %s", user_input_dict)

        # Call the predict function from the pipeline
        prediction = predict(user_input_dict)

        # Log the prediction result
        logger.info("Prediction result: %s", prediction)

        # Return the prediction result
        return {"prediction": int(prediction[0])}

    except Exception as e:
        # Log any errors that occur during the prediction process
        logger.error("Error occurred while processing the prediction: %s", str(e))
        return {"error": "An error occurred during prediction"}


@app.get('/test')
def test():
    return "yes this is working"




if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, log_level="info", reload=True)






