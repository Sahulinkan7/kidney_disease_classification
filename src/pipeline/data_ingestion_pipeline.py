from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

diconfig=DataIngestionConfig()
dt=DataIngestion(data_ingestion_config=diconfig)
print(dt.data_ingestion_config.root_dir)