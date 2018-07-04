from django.db import models
from django.contrib.auth.models import User
import string
import random


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


class FunStuff(models.Model):
    name = models.CharField(max_length=120)
    _CATEGORIES = [
        ("Entertainment", "Entertainment"),
        ("Food", "Food"),
        ('Drinks', "Drinks"),
        ("Outdoors", "Outdoors")
    ]
    category = models.CharField(
        max_length=13,
        choices=_CATEGORIES,
        default="Entertainment",
    )
    link = models.CharField(max_length=400)
    image_source = models.CharField(max_length=240)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fun Stuff"


class Local(models.Model):
    def getCode(size=24, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    name = models.CharField(max_length=120)
    relation = models.CharField(max_length=120)
    number = models.CharField(max_length=36,default=getCode, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Locals"


class Quote(models.Model):
    place = models.ForeignKey(FunStuff, on_delete=models.CASCADE)
    quote = models.CharField(max_length=120)
    user = models.ForeignKey(Local, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.place.name} - {self.user}'



