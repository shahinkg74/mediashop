from django.db import models


# Create your models here.
class etelaat(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    MobileNo = models.CharField(max_length=20)
    Adrresline1 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=15)

    objects = models.Manager()

    def __str__(self):
        return self.FirstName
