from gender_reaction_classifier.config import Configuration
from gender_reaction_classifier.constants import CONFIG_FILE_PATH

c=Configuration(CONFIG_FILE_PATH)
print(c.get_data_ingestion_config())

