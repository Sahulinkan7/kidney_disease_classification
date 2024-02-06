from django import forms 
from django.core.validators import FileExtensionValidator
from .models import ImagePredictionModel

class PredictionForm(forms.ModelForm):
    image = forms.ImageField(label="CT scan Image",widget=forms.FileInput(attrs={'class':'form-control'}),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])])
    class Meta:
        model = ImagePredictionModel
        fields=['image']