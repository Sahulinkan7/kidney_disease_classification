from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import PrepareBaseModelConfig
import os,sys
import tensorflow as tf
from pathlib import Path

class PrepareBaseModel:
    def __init__(self,prepare_base_model_config:PrepareBaseModelConfig):
        try:
            self.prepare_base_model_config = prepare_base_model_config
            os.makedirs(self.prepare_base_model_config.root_dir,exist_ok=True)
        except Exception as e:
            raise CustomException(e,sys)
    
    @staticmethod
    def save_model(path: Path,model : tf.keras.Model):
        try:
            logging.info(f"Saving model in file path {path}")
            model.save(path)
            logging.info(f"Model saved successfully")
        except Exception as e:
            logging.error(f"Exception occurred : Saving model interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def get_base_model(self):
        try:
            logging.info(f"Getting base model vgg16 from keras application ")
            os.makedirs(os.path.dirname(self.prepare_base_model_config.base_model_filepath),exist_ok=True)
            self.model=tf.keras.applications.vgg16.VGG16(
                input_shape = self.prepare_base_model_config.params_image_size,
                weights = self.prepare_base_model_config.params_weight,
                include_top = self.prepare_base_model_config.params_include_top
            )
            
            self.save_model(path=self.prepare_base_model_config.base_model_filepath,model=self.model)
        except Exception as e:
            logging.error(f"Exception occurred : getting base model interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    @staticmethod    
    def _prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        try:
            logging.info(f"preparing full model")
            if freeze_all:
                model.trainable= False
            elif (freeze_till is not None) and (freeze_till>0):
                for layer in model.layers[:-freeze_till]:
                    layer.trainable=False
                    
            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in)
            
            full_model = tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction
            )
            
            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss= tf.keras.losses.CategoricalCrossentropy(),
                metrics=['accuracy']
            )
            
            full_model.summary()
            logging.info(f"Full Model summary is as \n {full_model.summary()}")
            
            return full_model

        except Exception as e:
            logging.error(f"Exception occurred : preparing full model interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def update_base_model(self):
        try:
            logging.info(f"Updating base model")
            self.full_model = self._prepare_full_model(
                model=self.model,
                classes=self.prepare_base_model_config.params_classes,
                freeze_all=True,
                freeze_till=None,
                learning_rate=self.prepare_base_model_config.params_learning_rate
                
            )
            
            logging.info(f"saving updated base model")
            os.makedirs(os.path.dirname(self.prepare_base_model_config.updated_base_model_filepath),exist_ok=True)
            self.save_model(path=self.prepare_base_model_config.updated_base_model_filepath,model=self.full_model)
            
        except Exception as e:
            logging.error(f"Exception occurred : Updating base model interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)