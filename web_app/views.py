from django.shortcuts import render
from .forms import PredictionForm
# Create your views here.
from .models import ImagePredictionModel
from django.contrib import messages

def home_view(request):
    if request.method == 'POST':
        fm=PredictionForm(request.POST,request.FILES)
        if fm.is_valid():
            instance = ImagePredictionModel(image=fm.cleaned_data['image'],prediction=False)
            instance.save()
            image = ImagePredictionModel.objects.get(id=instance.id)
        else:
            messages.error(request,f"please upload an valid image")
    else:
        fm=PredictionForm()
        image = None
    return render(request,"core/homepage.html",{'form':fm,'image':image})