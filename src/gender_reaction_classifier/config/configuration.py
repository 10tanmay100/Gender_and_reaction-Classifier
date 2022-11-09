import os
from gender_reaction_classifier.utils import read_yaml,create_directory
from gender_reaction_classifier.entity import DataIngestionConfig
from pathlib import Path
import logging

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
            #creating all the paths for raw data ,train and test
            #here we do have two datasets so we create two directories in each dataset
            create_directory([self.config['data_ingestion'][files] for files in list(self.config['data_ingestion'].keys())[3:]])
            logging.info("all path directories created for data ingestion stage!!")
            return DataIngestionConfig(root_dir='data_ingestion',source_first_url=data_ingestion_config["data_source_one"],
            source_second_url=data_ingestion_config["data_source_second"],
            local_data_file_one=data_ingestion_config["local_data_file_one"],
            local_data_file_two=data_ingestion_config["local_data_file_two"],local_data_file_train_one=data_ingestion_config["local_data_file_train_one"],
            local_data_file_train_two=data_ingestion_config["local_data_file_train_two"],
            local_data_file_test_one=data_ingestion_config["local_data_file_test_one"],
            local_data_file_test_two=data_ingestion_config["local_data_file_test_two"])
        except Exception as e:
            logging.error(f"error while creatig configuration for data ingestion stage, error is {e}")






