from django.db import models

# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    modelName = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    year = models.IntegerField('Year Released')
    price = models.FloatField()
    
    def __str__(self):
        return f'{self.brand} ({self.modelName})'
