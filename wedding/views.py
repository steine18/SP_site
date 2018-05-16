from django.shortcuts import render
from .models import Hotel, Fund, FunStuff


# Create your views here.


def home(request):
    funds = Fund.objects.all()
    fun_stuff = FunStuff.objects.all()
    return render(request, 'wedding/save_the_date.html', {'funds': funds,
                                                          'fun_stuff' : fun_stuff,
                                                          })


def what_to_do(request):
    hotels = Hotel.objects.all()
    fun_stuff = {}
    categories = FunStuff.objects.order_by().values_list('category', flat = True).distinct()
    for cat in categories:
        fun_stuff[cat] = FunStuff.objects.filter(category = cat)
    return render(request, 'wedding/travel_tips.html', {'fun_stuff': fun_stuff,
                                                        'hotels': hotels,
                                                        'categories' : categories,
                                                       })

def what_to_do_detail(request, category):
    item = FunStuff.objects.filter(category = category.title())
    return render(request, 'wedding/what_to_do.html', {'item': item})
