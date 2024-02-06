from django.db import models

# Create your models here.

class ImagePredictionModel(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
    prediction = models.BooleanField(default=False)
