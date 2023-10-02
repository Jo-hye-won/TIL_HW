from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    label='제목',
    widget=forms.TextInput(
        attrs={
            'class': 'my-title',
        }
    )
)
    
class ArticleForm(forms.ModelForm):    
    # model 등록만 하면 끝남 # 모델폼에 모델을 등록
    class Meta:
        model = Article # Article모델 클래스를 등록
        fields = '__all__' # 전체 필드 선택
        # fields = ('title',) # title 필드만 포함
        # exclude = ('title',) # title 필드 제거 
        