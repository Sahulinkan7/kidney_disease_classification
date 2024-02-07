from django.shortcuts import render
from .forms import PredictionForm
# Create your views here.
from .models import ImagePredictionModel
from django.contrib import messages
from src.pipeline.prediction_pipeline import PredictionPipeline
from src.utils.commonutils import decodeImage
import os
from django.http import HttpResponse

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)
    
    
def train(request):
    if request.method == "POST":
        os.system("dvc repro")
    else:
        pass
    return render(request,"core/training.html")

def home_view(request):
    clApp = ClientApp()
    if request.method == 'POST':
        fm=PredictionForm(request.POST,request.FILES)
        if fm.is_valid():
            image = request.FILES['image']
            decodeImage(image, clApp.filename)
            result = clApp.classifier.predict()
            instance = ImagePredictionModel(image=fm.cleaned_data['image'],prediction=result)
            instance.save()
            image = ImagePredictionModel.objects.get(id=instance.id)
        else:
            messages.error(request,f"please upload an valid image")
    else:
        fm=PredictionForm()
        image = None
        result=None
    return render(request,"core/homepage.html",{'form':fm,'image':image,'result': result})