import os
from gender_reaction_classifier.utils import read_yaml,create_directory
from gender_reaction_classifier.entity import DataIngestionConfig
from pathlib import Path
import logging
from gender_reaction_classifier.constants import *

class Configuration:
    """
    This a configuration file which contains all the configuration of 
    the entire pipeline
    """
    def __init__(self, config_file_path:Path):
        #store the configuration file
        self.config_file_path = config_file_path
        #read the yaml file
        self.config = read_yaml(config_file_path)
    def get_data_ingestion_config(self):
        try:
            #calling all the folder paths from the yaml which we called in the initialization stage
            data_ingestion_config = self.config['data_ingestion']
            #defining the path to download to the first data from first data source url


            #creating all the paths for raw data ,train and test
            #here we do have two datasets so we create two directories in each dataset
            create_directory([self.config['data_ingestion'][files]+CURRENT_TIME for files in list(self.config['data_ingestion'].keys())[3:5]])
            logging.info("all path directories created for data ingestion stage!!")
            return DataIngestionConfig(root_dir='data_ingestion',source_first_url=data_ingestion_config["data_source_one"],
            source_second_url=data_ingestion_config["data_source_second"],
            local_data_file_one=os.path.join(data_ingestion_config["local_data_file_one"],CURRENT_TIME),
            local_data_file_two=os.path.join(data_ingestion_config["local_data_file_two"],CURRENT_TIME))
        except Exception as e:
            logging.error(f"error while creatig configuration for data ingestion stage, error is {e}")






