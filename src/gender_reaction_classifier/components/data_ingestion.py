import opendatasets as od
import os
from gender_reaction_classifier.entity import DataIngestionConfig
from tqdm import tqdm
from gender_reaction_classifier import logger
import datetime
from gender_reaction_classifier.constants import *

#defining the class for data ingestion
class DataIngestion:
    #now defining the inputs
    '''
    This class will reponsible to do some work to do data ingestion
    '''
    def __init__(self,config_file_path:DataIngestionConfig):
        self.data_ingestion_config=config_file_path
    def download_dataset(self):
        '''
        This method will responsible to download the data from the source which 
        I have mentioned in the data ingestion configuration
        '''
        try:
            #download the first data 
            od.download(dataset_id_or_url=self.data_ingestion_config.source_first_url,data_dir=self.data_ingestion_config.local_data_file_one)
            logger.info(f"Dataset downloaded from URL={self.data_ingestion_config.source_first_url} and download directory is {self.data_ingestion_config.local_data_file_one}")
            #download the second data 
            od.download(dataset_id_or_url=self.data_ingestion_config.source_second_url,data_dir=self.data_ingestion_config.local_data_file_two)
            logger.info(f"Dataset downloaded from URL={self.data_ingestion_config.source_first_url} and download directory is {self.data_ingestion_config.local_data_file_two}")
            return "Data Downloaded Successfully!!!"
        except Exception as e:
            logger.error(f"Isssue has happened while the data ingestion step...error is {e}")
        
        