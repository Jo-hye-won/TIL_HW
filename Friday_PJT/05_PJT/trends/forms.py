from django import forms
from .models import Keyword, Trend

class KeywordForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='키워드')
    class Meta:
        model = Keyword
        fields = '__all__'


class TrendForm(forms.ModelForm):
    class Meta:
        model = Trend
        fields = '__all__'
