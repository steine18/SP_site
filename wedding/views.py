from django.shortcuts import render
from .models import Hotel, Fund


# Create your views here.


def home(request):
    hotels = Hotel.objects.all()
    funds = Fund.objects.all()
    return render(request, 'wedding/save_the_date.html', {'hotels': hotels, 'funds': funds})


def registery(request):
    return render(request, 'wedding/base.html')
