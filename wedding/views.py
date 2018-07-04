from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Hotel, Fund, FunStuff, Quote, Local
from .forms import QuoteForm
import random


# Create your views here.
def home(request):
    hotels = Hotel.objects.all()
    funds = Fund.objects.all()
    return render(request, 'wedding/home.html', {'hotels': hotels, 'funds': funds})

def home2(request):
    funds = Fund.objects.all()
    fun_stuff = FunStuff.objects.all()
    return render(request, 'wedding/save_the_date.html', {'funds': funds,
                                                          'fun_stuff': fun_stuff,
                                                          })


def what_to_do(request):
    hotels = Hotel.objects.all()
    fun_stuff = {}
    categories = FunStuff.objects.order_by().values_list('category', flat=True).distinct()
    for cat in categories:
        fun_stuff[cat] = FunStuff.objects.filter(category = cat)
    quotes = {}
    for place in FunStuff.objects.all():
        qset = Quote.objects.filter(place = place, approved=True)
        if qset:
            quotes[place.name] = random.choice(qset)
    # For loop to iterate through each queryset and picking out quotes.
    return render(request, 'wedding/travel_tips.html', {'fun_stuff': fun_stuff,
                                                        'hotels': hotels,
                                                        'categories': categories,
                                                        'quotes': quotes})


def quote(request, number):
    local = get_object_or_404(Local, number = number)
    quotes = Quote.objects.filter(user = local)
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.approved = False
            post.user = Local.objects.get(name=local.name)
            post.save()
            return HttpResponseRedirect(f"/form/{number}/")
    else:
        form = QuoteForm()
    return render(request, 'wedding/forms.html', {'form': form,
                                                  'local': local,
                                                  'number': number,
                                                  'quotes': quotes,
                                                  })

def approve(request):
    locals = Local.objects.all()
    quotes = {}
    for local in locals:
        local_quotes = Quote.objects.filter(user = local)
        if local_quotes:
            quotes[local.name] = local_quotes


    return render(request, 'wedding/approve.html', {'locals' : locals,
                                                    'quotes' : quotes,
                                                    })