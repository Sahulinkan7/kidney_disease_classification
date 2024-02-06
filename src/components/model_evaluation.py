import os, sys
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig):
        try:
            self.model_evaluation_config = model_evaluation_config
        except Exception as e:
            raise CustomException(e, sys)
