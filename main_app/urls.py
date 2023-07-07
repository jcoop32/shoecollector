from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/', views.collection, name='collection'),
    path('collection/<int:shoe_id>/', views.shoe_details, name='details'),
    path('collection/create/', views.ShoeCreate.as_view(), name='shoe_create'),
    path('collection/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe_update'),
    path('collection/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe_delete'),
]