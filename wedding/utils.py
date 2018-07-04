from .models import FunStuff
from django.db import models
import os

def create_place(place):
    c,n,x,w,p = place
    place_entry = FunStuff.objects.create(name =n,
                                          category = c,
                                          link = w,
                                          image_source = p,
                                          info = '')

with open(os.getcwd() + 'wedding\FunStuff.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        if row[2] == 'x':
            create_place(row)
