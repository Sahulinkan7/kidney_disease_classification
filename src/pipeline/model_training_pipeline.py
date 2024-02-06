from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import ModeltrainerConfig
from src.logger import logging
from src.exception import CustomException
import os,sys


class ModelTrainerPipeline:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_model_training(self):
        try:
            trainer_config = ModeltrainerConfig()
            modeltraining = ModelTrainer(model_trainer_config=trainer_config)
            modeltraining.get_prepared_updated_base_model()
            modeltraining.train_valid_generator()
            modeltraining.start_training()
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
        
if __name__=="__main__":
    try:
        logging.info(f"{'=='*20} Model Trainer stage started {'=='*20}")
        model_trainer = ModelTrainerPipeline()
        model_trainer.initiate_model_training()
        logging.info(f"{'=='*20} Model Trainer stage  completed {'=='*20}")
    except Exception as e:
        logging.error(f"Model Trainer stage interrupted due to {CustomException(e,sys)}")
        raise CustomException(e,sys)