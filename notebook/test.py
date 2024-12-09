import sys
import os

# Add 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "src")))

# Test importing another module
try:
    import pandas as pd
    print("Pandas imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing pandas: {e}")

# Test importing a module from your project
try:
    from src.components.data_transformation import transform_features
    print("Data transformation module imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing from src.components.data_transformation: {e}")

# Try importing a random function from another file (e.g., a utility function)
try:
    from src.utils import some_function  # Make sure src/utils.py exists
    print("Function from utils imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing from src.utils: {e}")