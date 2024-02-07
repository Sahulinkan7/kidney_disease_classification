import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import os,sys
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import ModeltrainerConfig

class PredictionPipeline:
    def __init__(self,filename):
        try:
            self.filename=filename
        except Exception as e:
            raise CustomException(e,sys)
        
    def predict(self):
        try:
            model=load_model(ModeltrainerConfig.trained_model_filepath)
            imagename=self.filename
            test_image = image.load_img(imagename,target_size=(224,224))
            test_image_array = image.img_to_array(test_image)
            test_image_expand = np.expand_dims(test_image_array,axis=0)
            result = np.argmax(model.predict(test_image),axis=1)
            print(result)
            if result[0]==1:
                prediction = "Tumor"
                return prediction
            else:
                prediction = "Normal"
                return prediction
            
        except Exception as e:
            raise CustomException(e,sys)
        
        