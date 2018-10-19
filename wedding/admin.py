from django.contrib import admin
from .models import Hotel, Fund, FunStuff, Local, Quote, Event, Crawler


class QuoteAdmin(admin.ModelAdmin):
    search_fields = ['place', 'user']

    list_display = ('place', 'user', 'approved')

    list_editable = ['approved']

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Fund)
admin.site.register(FunStuff)
admin.site.register(Local)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Event)
admin.site.register(Crawler)

