#creating a function which will be resposible to read any kind of yaml file
from pathlib import Path
import os
from gender_reaction_classifier import logger
import yaml
def read_yaml(yaml_path:Path):
    '''
    This function will take yaml file path as an input
    and it will return the yaml object which we can use in the future
    as a dictionary in python.
    If it will return any error the reason will be mentioned as a output
    '''
    try:
        with open(yaml_path) as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        return f"Error has happened while reading yaml file, the error is {e}"
        
#creating function which will create directories
def create_directory(filepaths:list):
    """
    This directory will be responsible to create directory files
    It will take a list of paths as an input
    """
    try:
        for files in filepaths:
            logger.info(f"Reading the files ,{files}")
            os.makedirs(files,exist_ok=True)
    except Exception as e:
        return f"Issue has happened while creating directory, error is {e}"


