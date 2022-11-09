from dataclasses import dataclass
from pathlib import Path
#named entity defining for all the pipeline stage
#defining the the configuration for data ingestion stage

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for data ingestion stage
    """
    root_dir:str
    source_first_url:str
    source_second_url:str
    local_data_file_one:Path
    local_data_file_two:Path


