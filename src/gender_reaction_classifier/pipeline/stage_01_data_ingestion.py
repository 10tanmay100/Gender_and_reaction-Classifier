from gender_reaction_classifier.config import Configuration
from gender_reaction_classifier.constants import CONFIG_FILE_PATH
from gender_reaction_classifier.components import DataIngestion
from gender_reaction_classifier.entity import DataIngestionConfig
from gender_reaction_classifier import logger

def main():
    config=Configuration(CONFIG_FILE_PATH)
    data_ingestion_config=config.get_data_ingestion_config()
    DataIngestion_=DataIngestion(data_ingestion_config)
    print(DataIngestion_.download_dataset())


STAGE_NAME="DataIngestion"
if __name__ == "__main__":
    logger.info(f"{STAGE_NAME} has started!!")
    main()
    logger.info(f"{STAGE_NAME} has ended!!")