from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=120)
    website = models.CharField(max_length=220)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=64, default = "Las Vegas")
    state = models.CharField(max_length=2, default="NV")
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
