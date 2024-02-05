from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.logger import logging
from src.exception import CustomException
import os,sys

class DataIngestionTrainingPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Intitiating data ingestion stage in training pipeline")
            di=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            di.download_data()
            di.extract_data()
            logging.info("Data Ingestion pipeline inititation completed")
        except Exception as e:
            logging.error(f"Inititating data ingestion stage in training pipeline interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)


if __name__=="__main__":
    try:
        logging.info(f"{'=='*20} Data Ingestion stage started {'=='*20}")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logging.info(f"{'=='*20} Data Ingestion stage completed {'=='*20}")
    except Exception as e:
        logging.error(f"Data Ingestion stage interrupted due to {CustomException(e,sys)}")
        raise CustomException(e,sys)