from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Cheatsheet(models.Model):
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cheatsheets_detail', kwargs={'cheatsheet_id': self.id})

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(max_length=250)
    
    date = date.today()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cheatsheet = models.ForeignKey(Cheatsheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating
    
    # def get_absolute_url(self):
    #     return reverse('reviews_detail', kwargs={'pk': self.id})