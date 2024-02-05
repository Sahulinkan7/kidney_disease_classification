from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig
import urllib.request as request
import os,sys
import gdown
from zipfile import ZipFile

class DataIngestion:
    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            logging.info(f"Data Ingestion component Initiated")
            self.data_ingestion_config = data_ingestion_config
            os.makedirs(self.data_ingestion_config.root_dir,exist_ok=True)
        except Exception as e:
            logging.error(f"Creating data ingestion component object interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_data(self):
        try:
            logging.info(f"Downloading data from the source")
            os.makedirs(os.path.dirname(self.data_ingestion_config.downloaded_data_filepath),exist_ok=True)
            dataset_id = self.data_ingestion_config.data_download_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+dataset_id, self.data_ingestion_config.downloaded_data_filepath)
        except Exception as e:
            logging.error(f"data downloading interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def extract_data(self):
        try:
            logging.info(f"Extracting data from zip file ")
            os.makedirs(self.data_ingestion_config.extracted_data_filepath,exist_ok=True)
            with ZipFile(self.data_ingestion_config.downloaded_data_filepath,'r') as zipreference:
                zipreference.extractall(self.data_ingestion_config.extracted_data_filepath)
            logging.info(f"Data extracted to filepath {self.data_ingestion_config.extracted_data_filepath}")  
        except Exception as e:
            logging.error(f"data extraction interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    