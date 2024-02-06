from dataclasses import dataclass
from pathlib import Path
import os,sys 
from src.utils.commonutils import read_yaml
from src.constants import PARAMS_FILE_PATH

params_config = read_yaml(PARAMS_FILE_PATH)

@dataclass(frozen=True)
class TrainingPipelineConfig:
    root_dir : Path = os.path.join("artifacts")
    
    
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path = os.path.join(TrainingPipelineConfig.root_dir,"data_ingestion")
    data_download_url : str = f"https://drive.google.com/file/d/1zfrUjGq7pk7JrFMVhfdVdz2As1uYqX3q/view?usp=sharing"
    downloaded_data_filepath : Path = os.path.join(root_dir,"downloaded_data","data.zip")
    extracted_data_filepath : Path = os.path.join(root_dir,"extracted_data")
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir:Path = os.path.join(TrainingPipelineConfig.root_dir,"prepared_basemodel")
    base_model_filepath = os.path.join(root_dir,"base_model","basemodel.h5")
    updated_base_model_filepath = os.path.join(root_dir,"updated_basemodel","updatedbasemodel.h5")
    params_weight = params_config['WEIGHTS']
    params_image_size = params_config['IMAGE_SIZE']
    params_include_top = params_config['INCLUDE_TOP']
    params_classes= params_config['CLASSES']
    params_learning_rate = params_config['LEARNING_RATE']
    