import os 
from pathlib import Path 
import logging 


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "careerbot"

list_of_files = [
    ".github/workflows/.gitkeep", 
    "artifacts/"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/logger/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "config/params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass 
        logging.info(f"Creating empty file: {filepath}")
    else: 
        logging.info(f"{filename} already exists")
