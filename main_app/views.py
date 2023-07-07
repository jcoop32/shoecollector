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

def shoe_details(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'shoes/detail.html', {'shoe': shoe})