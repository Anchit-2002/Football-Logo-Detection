import os
from pathlib import Path
import logging

# Setting up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

project_name = "hate"
list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configurations/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py"
    "docker.py"
    "requirements.py"
    "setup.py"
    "Dockerfile"
    ".dockerignore"
]
import os
import logging
from pathlib import Path

# Setting up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

project_name = "hate"

list_of_files = [
    ("components", "__init__.py"),
    ("components", "data_ingestion.py"),
    ("components", "data_transformation.py"),
    ("components", "model_trainer.py"),
    ("pipeline", "__init__.py"),
    ("pipeline", "training_pipeline.py"),
    ("pipeline", "prediction_pipeline.py"),
    ("utils", "__init__.py"),
    ("utils", "common.py"),
    ("config", "__init__.py"),
    ("config", "configuration.py"),
    ("", "__init__.py"),
    ("", "exception.py"),
    ("", "logger.py"),
]

for (filedir, filename) in list_of_files:
    filepath = os.path.join(project_name, filedir, filename)
    filedir = os.path.join(project_name, filedir)

    if not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Creating directory: {filedir} for the file {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logger.info(f"Creating empty file: {filepath}")
    else:
        logger.info(f"{filename} already exists")

logger.info(f"Project structure created for {project_name}")
