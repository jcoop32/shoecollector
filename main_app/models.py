from django.db import models
from django.urls import reverse

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
    
    def __str__(self):
        return f'{self.brand} ({self.modelName})'
    def get_absolute_url(self):
        return reverse('details', kwargs={'shoe_id': self.id})
