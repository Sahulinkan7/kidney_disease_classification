from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import ModeltrainerConfig
import os, sys
from tensorflow import keras
import tensorflow as tf
from pathlib import Path
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model


class ModelTrainer:
    def __init__(self, model_trainer_config: ModeltrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise CustomException(e, sys)

    def get_prepared_updated_base_model(self):
        try:
            self.prepared_model: Model = keras.models.load_model(
                self.model_trainer_config.updated_basemodel_filepath
            )
        except Exception as e:
            raise CustomException(e, sys)

    def train_valid_generator(self):
        try:
            datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.20)
            dataflow_kwargs = dict(
                target_size=self.model_trainer_config.params_image_size[:-1],
                batch_size=self.model_trainer_config.params_batch_size,
                interpolation="bilinear",
            )

            logging.info(f"creating validation data")
            valid_datagenerator_object = ImageDataGenerator(**datagenerator_kwargs)

            self.valid_generator = valid_datagenerator_object.flow_from_directory(
                directory=self.model_trainer_config.training_data,
                subset="validation",
                shuffle=False,
                **dataflow_kwargs,
            )

            logging.info(f"creating training data")

            if self.model_trainer_config.params_is_augmentation:
                train_datagenerator_object = ImageDataGenerator(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2,
                    **datagenerator_kwargs,
                )
            else:
                train_datagenerator_object = valid_datagenerator_object

            self.train_generator = train_datagenerator_object.flow_from_directory(
                directory=self.model_trainer_config.training_data,
                subset="training",
                shuffle=True,
                **dataflow_kwargs,
            )
        except Exception as e:
            raise CustomException(e, sys)

    def start_training(self):
        try:
            logging.info(f"Starting model Training ")
            self.steps_per_epoch = (
                self.train_generator.samples // self.train_generator.batch_size
            )
            self.validation_steps = (
                self.train_generator.samples // self.valid_generator.batch_size
            )

            self.prepared_model.fit(
                self.train_generator,
                epochs=self.model_trainer_config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.valid_generator,
            )

            os.makedirs(
                os.path.dirname(self.model_trainer_config.trained_model_filepath),
                exist_ok=True,
            )
            self.save_model(
                path=self.model_trainer_config.trained_model_filepath,
                model=self.prepared_model,
            )
            logging.info(f"Model Training completed")
        except Exception as e:
            logging.info(f"Model Training interrupted due to {CustomException(e,sys)}")
            raise CustomException(e, sys)

    @staticmethod
    def save_model(path: Path, model: Model):
        try:
            logging.info(f"Saving model in file path {path}")
            model.save(path)
            logging.info(f"Model saved successfully")
        except Exception as e:
            logging.error(f"Saving model interrupted due to {CustomException(e,sys)}")
            raise CustomException(e, sys)
