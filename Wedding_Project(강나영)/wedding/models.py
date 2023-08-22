from django.db import models

# Create your models here.

class Wedding(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'