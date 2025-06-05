import os
from pathlib import Path


list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "scr/components/__init__.py",
    "scr/components/data_ingestion.py",
    "scr/components/data_transformation.py",
    "scr/components/model_trainer.py",
    "scr/components/model_evaluation.py",
    "scr/pipeline/__init__.py",
    "scr/pipeline/training_pipeline.py",
    "scr/pipeline/prediction_pipeline.py",
    "scr/utils/__init__.py",
    "scr/utils/utils.py",
    "scr/logger/logging.py",
    "scr/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.inl",
    "experiment/experiments.ipynb"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        #logging.info(f"Creating directory:{filedir} for file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass