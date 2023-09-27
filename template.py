import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "restaurant_rating_prediction"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/logging.py",
    f"src/{project_name}/utils.py",
    f"setup.py",
    f"requirements.txt",
    f"app.py",
    f"main.py",
    f"Dockerfile"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"{filepath} is already exists.")

        