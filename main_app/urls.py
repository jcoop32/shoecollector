from django.urls import path
from . import views

# find out how to pass in string as the path for specific username

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/', views.collection, name='collection'),
    path('explore/', views.explore_page, name='explore_page'),
    path('collection/<int:shoe_id>/', views.shoe_details, name='details'),
    path('collection/create/', views.ShoeCreate.as_view(), name='shoe_create'),
    path('collection/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe_update'),
    path('collection/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('shoes/<int:shoe_id>/like/', views.like_shoe, name='like_shoe'),
    path('user/<slug:username>/', views.users_collection, name='user_collection'),
]