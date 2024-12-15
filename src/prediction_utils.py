
def calculate_bmi(weight:float, height:float )-> float:
    """
    calculating the bmi given the height and weight 
    
    parameters:
    - weight (float) the weight of the user in kilograms
    - height (float) the height of the user in centimeters
    
    returns:
    - float value -> the calculated bmi
    
    sidenote: transforms the height first to meters
    """
    # Convert height from cm to meters
    height_meters = height / 100
    
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    
    return round(bmi, 2)



def calculate_health_days(physical_health_days:int, mental_health_days:int) -> int:
    """_summary_

    Args:
        physical_health_days (int): refer to the days on how many days an individual is 
        suffering physical issues in the past 30 days
        
        mental_health_days (int): refer to the days on how many days an individual is 
        suffering mental issues in the past 30 days 

    Returns:
        int: returns the aggregated healthdays of the two values
    """
    
    health_days = physical_health_days + mental_health_days
    
    return health_days

def calculate_lifestyle_score(smoker_status: int, e_cigarette_usage: int, alcohol_drinker: int, 
                              physical_activity: int, removed_teeth: int, sleep_hours: float) -> float:
    '''
    Calculate the lifestyle score based on various health behaviors and conditions.
    
    Parameters:
    - smoker_status (int): Smoker status (0 - Never, 1 - Former, 2 - Some days, 3 - Every day)
    - e_cigarette_usage (int): E-cigarette usage (0 - Never, 1 - Never used, 2 - Some days, 3 - Every day)
    - alcohol_drinker (int): Alcohol consumption (0 - No, 1 - Yes)
    - physical_activity (int): Physical activity (0 - No, 1 - Yes)
    - removed_teeth (int): Number of teeth removed (0 - None, 1-5, 6+)
    - sleep_hours (float): Hours of sleep per day
    
    Returns:
     score (float): Lifestyle score based on the input values
    '''
    score = 0
    
    # Smoker Status
    if smoker_status == 3:  # Current smoker - now smokes every day
        score -= 1
    elif smoker_status == 2:  # Current smoker - smokes some days
        score -= 0.5
    elif smoker_status == 1:  # Former smoker
        score += 0  # Neutral for former smokers
    elif smoker_status == 0:  # Never smoked
        score += 1

    # E-Cigarette Usage (Vaping)
    if e_cigarette_usage == 3:  # Use e-cigarettes every day
        score -= 1
    elif e_cigarette_usage == 2:  # Use e-cigarettes some days
        score -= 0.5
    elif e_cigarette_usage == 1:  # Never used e-cigarettes in my entire life
        score += 0  # Neutral for non-users
    elif e_cigarette_usage == 0:  # Not at all (right now)
        score += 1

    # Alcohol Drinkers
    if alcohol_drinker == 1:  # Alcohol drinker
        score -= 1
    elif alcohol_drinker == 0:  # Non-alcohol drinker
        score += 1

    # Physical Activity
    if physical_activity == 0:  # No physical activity
        score -= 1
    elif physical_activity == 1:  # Any physical activity
        score += 1

    # Removed Teeth
    if removed_teeth == 0:  # No teeth removed
        score += 1
    elif 1 <= removed_teeth <= 1:  # 1 to 5 teeth removed
        score += 0  # Neutral
    elif 2 <= removed_teeth <= 2:  # 6 or more, but not all teeth removed
        score -= 0.5
    elif removed_teeth == 3:  # All teeth removed
        score -= 1

    # Sleep Hours
    if sleep_hours < 6:  # Less than 6 hours of sleep
        score -= 1
    elif sleep_hours > 10:  # More than 10 hours of sleep
        score -= 1
    elif 7 <= sleep_hours <= 9:  # Optimal sleep (7-9 hours)
        score += 1
    else:  # Between 6 and 7, or between 9 and 10 hours of sleep
        score += 0  # Neutral

    return score

def calculate_chronic_disease_score(had_stroke: int, had_copd: int, had_diabetes: int, had_arthritis: int, 
                                    had_kidney_disease: int, had_skin_cancer: int, had_asthma: int) -> int:
   
    '''
    Calculate the chronic disease score based on the presence of various chronic conditions.
    
    Parameters:
    - had_stroke (int): 1 if the user had a stroke, 0 otherwise
    - had_copd (int): 1 if the user had COPD, 0 otherwise
    - had_diabetes (int): 1 if the user had diabetes, 0 otherwise
    - had_arthritis (int): 1 if the user had arthritis, 0 otherwise
    - had_kidney_disease (int): 1 if the user had kidney disease, 0 otherwise
    - had_skin_cancer (int): 1 if the user had skin cancer, 0 otherwise
    - had_asthma (int): 1 if the user had asthma, 0 otherwise
    
    Returns:
    - chronic_disease_score (int): Chronic disease score based on the user's conditions.
    '''
    
    # Calculate chronic disease score usisng multiplicative interaction
    chronic_disease_score = (
        (had_stroke + 1) * (had_copd + 1) * (had_diabetes + 1) * (had_arthritis + 1) *
        (had_kidney_disease + 1) * (had_skin_cancer + 1) * (had_asthma + 1)
    )
    
    return chronic_disease_score

def map_age(age: int) -> int:
    """
    Maps the user's age to the corresponding age category based on predefined ranges.
    
    Parameters:
    - age (int): The age of the user.
    
    Returns:
    - int: The mapped integer value for the age category.
    """
    if 0 <= age <= 17:
        return 0  # Return 0 for ages 0 to 17
    elif 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    elif age >= 80:
        return 13
    else:
        return None  # In case of invalid age (less than 0), return None