from setuptools import setup, find_packages
from typing import List



def get_requirements(file_path:str) -> List[str]:
    """
    this function will return the list of packages requirements
    """
    requirements = []
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")


setup(

    
    version="1.0.0",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    name="Heart_Disease_Predictor",
    description='A heart disease prediction model',
    author="exis001",
    author_email="allecsisgarcia001@gmail.com",
    url="https://github.com/exis000/HeartDiseasePredictor_Model"
)