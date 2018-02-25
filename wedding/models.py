from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=120)
    website = models.CharField(max_length=220)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=64, default="Las Vegas")
    state = models.CharField(max_length=2, default="NV")
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Fund(models.Model):
    name = models.CharField(max_length=120)
    link = models.CharField(max_length=400)
    info = models.TextField(blank=True)
    image_source = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    name = models.CharField(max_length=120)
    CATEGORIES = [
        ("Entertainment", "Entertainment"),
        ("Food", "Food"),
        ("Outdoors", "Outdoors")
    ]
    category = models.CharField(
        max_length=13,
        choices=CATEGORIES,
        default="Entertainment",
    )
    link = models.CharField(max_length=400)
    image_source = models.CharField(max_length=120)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name
