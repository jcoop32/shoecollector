from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
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
    return render(request, 'shoes/details.html', {'shoe': shoe})

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = '__all__'


class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/collection'
