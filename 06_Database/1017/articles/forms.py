from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        # fields = '__all__'
        # exclude = ('user', 'like_users',)