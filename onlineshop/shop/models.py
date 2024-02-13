from django.db import models


# Create your models here.
class kharid(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="static/images/%y")
    price = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.title
