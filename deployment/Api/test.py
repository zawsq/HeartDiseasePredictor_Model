import requests

# Define the URL for the predict endpoint
url = "http://127.0.0.1:8000/predict"

# Define the data you want to send (make sure it matches the HeartDiseaseInput schema)
data = {
  "Age":18,
  "Height": 175.5,
  "Weight": 1000,
  "HadAngina": 0,
  "PhysicalHealthDays": 30,
  "MentalHealthDays":30,
  "SmokerStatus": 1,
  "ECigaretteUsage": 0,
  "AlcoholDrinker": 1,
  "PhysicalActivities": 0,
  "RemovedTeeth": 6,
  "SleepHours": 20,
  "HadStroke": 0,
  "HadCOPD": 0,
  "HadDiabetes": 1,
  "HadArthritis": 0,
  "HadKidneyDisease": 0,
  "HadSkinCancer": 1,
  "HadAsthma": 1
}

# Send the POST request with the data
response = requests.post(url, json=data)

# Check the response status and print the result
if response.status_code == 200:
    print("Prediction:", response.json())  # Print the prediction result from the API
else:
    print("Error:", response.status_code, response.text)