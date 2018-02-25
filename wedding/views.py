from django.shortcuts import render
from .models import Hotel, Fund, ToDo


# Create your views here.


def home(request):
    hotels = Hotel.objects.all()
    funds = Fund.objects.all()
    food = ToDo.objects.filter(category = 'Food')
    outdoors = ToDo.objects.filter(category = 'Otdoors')
    entertainment = ToDo.objects.filter(category = 'Entertainment')
    categories = set([todo.category for todo in ToDo.objects.all()])
    todos = {cat : ToDo.objects.filter(category = cat) for cat in categories}
    return render(request, 'wedding/save_the_date.html', {'hotels': hotels,
                                                          'funds': funds,
                                                          'categories' : categories,
                                                          'todos': todos,
                                                          'food': food,
                                                          'outdoors' : outdoors,
                                                          'entertainment' : entertainment,
                                                          })


def what_to_do(request):
    food = ToDo.objects.filter(category="Food")
    entertainment = ToDo.objects.filter(category='Entertainment')
    todos = ToDo.objects.filter(category='Outdoors')

    #todos = ['food', 'ent', 'out']
    return render(request, 'wedding/what_to_do.html', {'todos': todos,
                                                       })

def what_to_do_detail(request, category):
    item = ToDo.objects.filter(category = category.title())
    return render(request, 'wedding/what_to_do.html', {'item': item})
