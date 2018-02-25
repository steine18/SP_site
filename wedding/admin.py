from django.contrib import admin
from .models import Hotel, Fund, ToDo

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Fund)
admin.site.register(ToDo)