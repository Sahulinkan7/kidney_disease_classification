from src.components.prepare_basemodel import PrepareBaseModel
from src.entity.config_entity import PrepareBaseModelConfig
from src.logger import logging
from src.exception import CustomException
import os,sys

class PrepareBaseModelPipeline:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_prepare_base_model(self):
        try:
            base_model_config = PrepareBaseModelConfig()
            basemodel = PrepareBaseModel(prepare_base_model_config=base_model_config)
            basemodel.get_base_model()
            basemodel.update_base_model()
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__=="__main__":
    try:
        logging.info(f"{'=='*20} Prepare Base model stage started {'=='*20}")
        base_model_preparation = PrepareBaseModelPipeline()
        base_model_preparation.initiate_prepare_base_model()
        logging.info(f"{'=='*20} Prepare Base Model stage completed {'=='*20}")
    except Exception as e:
        raise CustomException(e,sys)
