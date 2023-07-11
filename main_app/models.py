from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# options for sneaker type
typesOfShoes = (
    ('Sneakers', 'Sneakers'),
    ('Casual', 'Casual'),
    ('Boots', 'Boots'),
    ('Athletic', 'Athletic'),
)

class Shoe(models.Model):
    # fields and attributes
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
    
class Comment(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.shoe.brand} ({self.shoe.modelName})'
