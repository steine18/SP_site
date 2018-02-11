from django.shortcuts import render
from .models import Hotel


# Create your views here.


def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'wedding/save_the_date.html', {'hotels': hotels})


def registery(request):
    return render(request, 'wedding/base.html')
