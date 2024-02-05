from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig

import os,sys

class DataIngestion:
    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            os.makedirs(self.data_ingestion_config.root_dir,exist_ok=True)
        except Exception as e:
            raise CustomException(e,sys)
        
    def download_data(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)