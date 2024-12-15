from pydantic import BaseModel


class HeartDiseaseInput(BaseModel):
    Age: int  # Age of the user
    Height: float  # Height in cm
    Weight: float  # Weight in kg
    HadAngina: int  # yes = 1 , no = 0
    
    # health days
    PhysicalHealthDays: int  # Number of days the user experienced physical health issues
    MentalHealthDays: int  # Number of days the user experienced mental health issues
    
    # lifestyle
    SmokerStatus: int  # Options: 0 = "Never", 1 = "Former", 2 = "Current"
    ECigaretteUsage: int  # Options: 0 = "Never", 1 = "Former", 2 = "Current"
    AlcoholDrinker: int  # 0 = yes , 0 = no
    PhysicalActivities: int  # 0 = yes , 0 = no
    RemovedTeeth: int  # Options: 0 = "None", 1 = "1-5", 2 = "6+", 3 = "All"
    SleepHours: float  # Hours of sleep per night
    
    # Chronic disease indicators
    HadStroke: int  # 0 = No, 1 = Yes
    HadCOPD: int  # 0 = No, 1 = Yes
    HadDiabetes: int  # 0 = No, 1 = Yes
    HadArthritis: int  # 0 = No, 1 = Yes
    HadKidneyDisease: int  # 0 = No, 1 = Yes
    HadSkinCancer: int  # 0 = No, 1 = Yes
    HadAsthma: int  # 0 = No, 1 = Yes
    
    
    
    
    
    
    
    
    
    
    
    
    