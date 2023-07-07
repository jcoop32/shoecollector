from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/', views.collection, name='collection'),
    path('collection/<int:shoe_id>/', views.shoe_details, name='details'),
]