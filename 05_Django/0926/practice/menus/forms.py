from django import forms
from .models import Menu

# 파이썬에서 class의 이름을 정의하는 name convention은
# 파스칼 케이슫

class MenuForm(forms.modelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        # fields = ('neme', 'price', )
        # exclude = ('price')