from flask import Flask, render_template, request
import requests

website = Flask(__name__)


@website.route('/')
def home():
    return render_template("predict.html")

@website.route("/about_the_model")
def about_the_model():
    return render_template("about_the_model.html")










@website.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        form_data = request.form.to_dict()
        print(form_data)  # Debug: Check form data

        # Validate and process form data
        processed_data = {
            "Age": int(form_data["Age"]) if form_data.get("Age") else 0,  # No default for Age
            "Height": max(0, float(form_data["Height"])) if form_data.get("Height") else 0,  # No default for Height
            "Weight": max(0, float(form_data["Weight"])) if form_data.get("Weight") else 0,  # No default for Weight
            "HadAngina": int(form_data.get("HadAngina", 0)),  # Default to 0 if not provided
            "PhysicalHealthDays": max(0, min(30, int(form_data.get("PhysicalHealthDays", 0)))),  # Default to 0 if not provided
            "MentalHealthDays": max(0, min(30, int(form_data.get("MentalHealthDays", 0)))),  # Default to 0 if not provided
            "SmokerStatus": int(form_data.get("SmokerStatus", 0)),  # Default to 0 if not provided
            "ECigaretteUsage": int(form_data.get("ECigaretteUsage", 0)),  # Default to 0 if not provided
            "AlcoholDrinker": int(form_data.get("AlcoholDrinker", 0)),  # Default to 0 if not provided
            "PhysicalActivities": int(form_data.get("PhysicalActivities", 0)),  # Default to 0 if not provided
            "RemovedTeeth": int(form_data.get("RemovedTeeth", 0)),  # Default to 0 if not provided
            "SleepHours": max(0, float(form_data.get("SleepHours", 0))),  # Default to 0 if not provided
            "HadStroke": int(form_data.get("HadStroke", 0)),  # Default to 0 if not provided
            "HadCOPD": int(form_data.get("HadCOPD", 0)),  # Default to 0 if not provided
            "HadDiabetes": int(form_data.get("HadDiabetes", 0)),  # Default to 0 if not provided
            "HadArthritis": int(form_data.get("HadArthritis", 0)),  # Default to 0 if not provided
            "HadKidneyDisease": int(form_data.get("HadKidneyDisease", 0)),  # Default to 0 if not provided
            "HadSkinCancer": int(form_data.get("HadSkinCancer", 0)),  # Default to 0 if not provided
            "HadAsthma": int(form_data.get("HadAsthma", 0)),  # Default to 0 if not provided
        }

        # Send the processed data to the FastAPI /predict endpoint
        api_url = "http://127.0.0.1:8000/predict"  # Your FastAPI endpoint
        response = requests.post(api_url, json=processed_data)

        # Handle the API response
        if response.status_code == 200:
            prediction = response.json().get("prediction", "No result")
        else:
            prediction = f"Error: {response.json().get('error', 'Unable to get a prediction')}"

        return render_template('predict.html', prediction=prediction)

    except Exception as e:
        # Catch unexpected errors and display a user-friendly message
        return render_template('predict.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    
    website.run(debug=True)