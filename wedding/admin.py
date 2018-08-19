from django.contrib import admin
from .models import Hotel, Fund, FunStuff, Local, Quote


class QuoteAdmin(admin.ModelAdmin):
    search_fields = ['place', 'user']

    list_display = ('place', 'user', 'approved')


# Register your models here.
admin.site.register(Hotel)
admin.site.register(Fund)
admin.site.register(FunStuff)
admin.site.register(Local)
admin.site.register(Quote, QuoteAdmin)

