from dataclasses import dataclass
from pathlib import Path
import os,sys 
from src.utils.commonutils import read_yaml

@dataclass(frozen=True)
class TrainingPipelineConfig:
    root_dir : Path = os.path.join("artifacts")
    
    
@dataclass
class DataIngestionConfig:
    root_dir : Path = os.path.join(TrainingPipelineConfig.root_dir,"data_ingestion")
    data_download_url : str = f"https://drive.google.com/file/d/1zfrUjGq7pk7JrFMVhfdVdz2As1uYqX3q/view?usp=sharing"
    downloaded_data_filepath : Path = os.path.join(root_dir,"downloaded_data","data.zip")
    extracted_data_filepath : Path = os.path.join(root_dir,"extracted_data")