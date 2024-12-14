

import zipfile

file_name = "model/RandomForest_best_model.pkl"  # Path to your model file
zip_file_name = "RandomForest_best_model.zip"   # Output zip file name

with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add file to the zip archive
    # Use arcname to exclude the "model/" prefix in the zip file if desired
    zipf.write(file_name, arcname="RandomForest_best_model.pkl")