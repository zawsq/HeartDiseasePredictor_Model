# Heart Disease Prediction Using Machine Learning

## Overview
This project aims to predict the likelihood of heart disease based on various health and lifestyle indicators. Using machine learning models, I developed a robust solution that tackles several key challenges often encountered in real-world datasets, such as class imbalance, missing data, combining data, feature importance and interaction. The primary goal is to build a model that can effectively predict heart disease, while also prioritizing recall, which is crucial in medical applications to avoid false negatives.

The project utilizes an ensemble of models, such as RandomForest, CatBoost, LightGBM, and XGBoost, to handle the complexity and non-linear relationships within the data. The final model demonstrates high performance, with a focus on making accurate predictions for both healthy individuals and those with heart disease.

## Why This Project?
Heart disease is one of the leading causes of death worldwide, and early detection is critical for effective treatment. I chose this project to showcase my ability to apply machine learning techniques to a real-world healthcare problem, addressing challenges such as imbalanced datasets and data inconsistencies. The project is also a demonstration of how to handle large datasets and implement a great model pipeline and structure that you should follow.

In addition, this project serves as a learning resource for aspiring data scientists, providing clear explanations of each step in the data science pipeline—from data ingestion to model deployment. The goal is to make the project accessible to beginners while also incorporating advanced techniques used in professional data science projects and i recommend to check my jupyter notebook for clear information about each of the steps done.

**links to my jupyter notebooks**

[Link to my Jupyter Notebook part one - preprocessing, exploratory data analysis](./notebook/EDA.ipynb)

[Link to my Jupyter Notebook part two - feature scaling, model training, hyperparameter tuning and resampling techniques ](./notebook/model_training.ipynb)


## Problem Statement
The dataset contains various health and lifestyle features that are used to predict the likelihood of heart disease. The target variable (HeartDisease) is highly imbalanced, with a distribution of 95% healthy and 5% heart disease, which poses a challenge for training an effective machine learning model. This project addresses several challenges, including:

- **Class Imbalance**: The target variable has a severe class imbalance, making it difficult for models to learn the minority class (heart disease).
- **Handling Missing Data**: The dataset contains missing values, which are addressed using advanced imputation techniques.
- **Feature Importance**: Understanding which features have the most significant impact on the prediction.
- **Non-Linear Relationships**: Many features have non-linear relationships, which are better captured by ensemble models.

## Dataset
The dataset used in this project is sourced from Kaggle, and it includes health-related data collected by the 2022 annual CDC survey data of 400k+ adults related to their health status.

'''According to the CDC, heart disease is a leading cause of death for people of most races in the U.S. (African Americans, American Indians and Alaska Natives, and whites). About half of all Americans (47%) have at least 1 of 3 major risk factors for heart disease: high blood pressure, high cholesterol, and smoking. Other key indicators include diabetes status, obesity (high BMI), not getting enough physical activity, or drinking too much alcohol. Identifying and preventing the factors that have the greatest impact on heart disease is very important in healthcare. In turn, developments in computing allow the application of machine learning methods to detect "patterns" in the data that can predict a patient's condition.

The dataset originally comes from the CDC and is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to collect data on the health status of U.S. residents. As described by the CDC: "Established in 1984 with 15 states, BRFSS now collects data in all 50 states, the District of Columbia, and three U.S. territories. BRFSS completes more than 400,000 adult interviews each year.'''

you can find more info about the dataset in this link right here
[Source:](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease)


The dataset consists of three files:

- **2020 dataset**: 300k rows, 12 features.
- **2022 dataset**: Two versions (one with missing values and one without), each containing 300k+ rows and 40 features.

The features include various health indicators such as age, weight, smoking status, physical activity, and chronic diseases. The target variable is **HeartDisease**, which indicates whether the individual has heart disease.

## Project Workflow
The project is structured in a modular pipeline to ensure flexibility and scalability. The workflow includes the following stages:

1. **Data Ingestion and Data transformation**
    - **Feature encoding**: All features are properly implemented
    - **Missing Data**: Missing values are handled using MICE imputation, which leverages the relationships between features to predict and fill missing values.
    - **Class Imbalance**: Various techniques are applied to address the severe class imbalance, including class weights, manual and auto resampling, and techniques such as SMOTE, ADASYN AND ENN.
    - **Feature Selection**: Based on insights gained from Exploratory Data Analysis (EDA) and correlation analysis, the most relevant features are selected, and interactions between features are created to improve model performance.
    - **Feature Scaling**: The features are standardized to ensure they are on the same scale, improving model performance.

3. **Model Selection and Training**
    - **Models Used**: A combination of models is used to evaluate performance:
        - Logistic Regression (for linear relationship comparison)
        - CatBoost, LightGBM, RandomForest, XGBoost (ensemble methods for better handling of non-linear relationships)
    - **Model Evaluation**: Models are evaluated based on recall and precision, with a particular focus on recall, as it is crucial in medical applications to avoid false negatives.
    - **Best Model**: The RandomForest model performed the best, achieving:
        - 99% recall and precision for healthy individuals.
        - 85% recall and 70% precision for individuals with heart disease, significantly improving over the baseline models that only has 20% recall and 60% precision due to imbalance.

4. **Model Deployment**
    - The final model is deployed using a Fast API, allowing users to input health data and receive heart disease predictions.
    - The API is integrated with a simple website where users can input their data, and predictions are displayed in real-time.

## Key Insights and Learnings
- **Handling Class Imbalance**: This project emphasizes the importance of addressing class imbalance, which can significantly impact the performance of machine learning models. Techniques like resampling, class weights, and SMOTE were essential for improving the recall for the minority class (heart disease).
- **Feature Importance**: By using various feature selection techniques and evaluating models based on feature importance, I was able to identify which health indicators were most predictive of heart disease.
- **Exploratory Data Analysis (EDA)**: Conducting thorough EDA allowed me to gain valuable insights into the dataset, helping with feature selection and the creation of new features.
- **Model Deployment**: This project was not just about building a model but also about making it accessible to users. Deploying the model as an API and creating a simple user-friendly website demonstrated my ability to bring machine learning solutions to production.

## Future Improvements
- **Deep Learning**: Adding deep learning models, such as neural networks, could further improve performance.
- **Risk Factor Prediction**: Developing a health consultation system that provides personalized risk factor predictions based on the classification result could be a valuable addition.
- **User Feedback**: Implementing a feedback system where users can input additional data or track their health over time could help improve the model’s predictions.

## Conclusion
This project has been an invaluable learning experience, particularly in terms of handling imbalanced datasets, feature importance, and model deployment. By following a structured workflow, I was able to take the project from data ingestion all the way to deployment. The project is designed to be easily extendable, meaning that the same pipeline could be applied to other classification problems beyond heart disease.

## Files and Folder Structure
- **src/**: Contains all source code, file logging, utils, including data ingestion, transformation, and model training pipelines that you can run in one go that does all the steps.
- **deployment/**: Contains the fast API and flask website for deployment.
- **notebooks/**: Jupyter notebooks documenting the EDA(contains preprocessing, feature selection, cleaning) , model training(hyperparameter tuning , scaling, resampling and evaluation).
- **data/**: The raw and processed(cleaned) datasets used in the project.
- **model/**: This folder contains the model that is saved standard scaler, and our prediction model

## How to Run the Project
1. Clone this repository:
    ```bash
    git clone https://github.com/exis000/HeartDiseasePredictor_Model
    ```
2. Navigate to the project directory:
    ```bash
    cd heart-disease-prediction
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Extract the zipped model in model folder



"This project reflects my understanding of data science practices. I'm always open to constructive feedback to improve further. Thank you so much! ๑•⩊•๑"
