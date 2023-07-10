from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import requests
typesOfShoes = (
    ('Sneakers', 'Sneakers'),
    ('Casual', 'Casual'),
    ('Boots', 'Boots'),
    ('Athletic', 'Athletic'),
)

# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    modelName = models.CharField(max_length=100, verbose_name='Model Name')
    type = models.CharField(max_length=20, choices=typesOfShoes, default=typesOfShoes[0][0])
    colorway = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    year = models.IntegerField('Year Released')
    price = models.FloatField()
    img = models.CharField(max_length=250)
    likes = models.ManyToManyField(User, related_name='liked_shoes', blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.brand} ({self.modelName})'
    def get_absolute_url(self):
        return reverse('details', kwargs={'shoe_id': self.id})


# def apiCall(shoe):
#     url = "https://sneaker-database-stockx.p.rapidapi.com/getproducts"

#     querystring = {"keywords": shoe,"limit":"1"}

#     headers = {
# 	"X-RapidAPI-Key": "572f50d378msh021a6af858f5f25p163927jsn0cfc2ef4568b",
# 	"X-RapidAPI-Host": "sneaker-database-stockx.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     return response.json()