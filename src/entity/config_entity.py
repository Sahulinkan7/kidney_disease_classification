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
    