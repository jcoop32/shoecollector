from django.shortcuts import render
from .models import Shoe

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def collection(request):
    shoes = Shoe.objects.all()  # Assuming each shoe is associated with a user
    return render(request, 'shoes/collection.html', {'shoes': shoes})