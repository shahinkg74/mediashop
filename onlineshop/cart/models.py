from django.db import models


# Create your models here.
class kart(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    total = models.CharField(max_length=10)

    def __str__(self):
        return self.name
