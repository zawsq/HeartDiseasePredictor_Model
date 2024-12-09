import os
import sys

def set_project_root():
   PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
   if PROJECT_ROOT not in sys.path:  # Avoid adding the same path multiple times
        sys.path.append(PROJECT_ROOT)
