import os
from pathlib import Path

list_of_files = [
    ".github/workdir/.gitkeep", # continuous integration / continuous deployment (CI/CD)
    # "packaging ml model/__init__.py",
    "packaging ml model/MANIFEST.in",
    "packaging ml model/prediction_model/__init__.py",
    "packaging ml model/prediction_model/config/__init__.py",
    "packaging ml model/prediction_model/config/config.py",
    "packaging ml model/prediction_model/pipeline.py",
    "packaging ml model/prediction_model/predict.py",
    "packaging ml model/prediction_model/processing/__init__.py",
    "packaging ml model/prediction_model/processing/data_handling.py",
    "packaging ml model/prediction_model/processing/preprocessing.py",
    "packaging ml model/prediction_model/trained_models/__init__.py",
    "packaging ml model/prediction_model/training_pipeline.py",
    "packaging ml model/prediction_model/datasets/__init__.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # Create an empty file