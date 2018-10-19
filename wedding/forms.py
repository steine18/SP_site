from django import forms
from . import models


class QuoteForm(forms.ModelForm):
    class Meta:
        model = models.Quote
        fields = [
            'place',
            'quote',
        ]

class EditQuoteForm(forms.ModelForm):
    class Meta:
        model = models.Quote
        fields = [
            'place',
            'quote',
            'approved',
        ]

class BarCrawlForm(forms.ModelForm):
    class Meta:
        model = models.Crawler
        fields = [
            'name',
            'count',
        ]