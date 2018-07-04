from django.contrib import admin
from .models import Hotel, Fund, FunStuff, Local, Quote

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Fund)
admin.site.register(FunStuff)
admin.site.register(Local)
admin.site.register(Quote)