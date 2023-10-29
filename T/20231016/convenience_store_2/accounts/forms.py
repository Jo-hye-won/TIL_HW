from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
                # get_user_model() 
                # => 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 함수 
                # User로 해도 지금은 큰 변화 없지만 나중에 많아지면 직접참조하지 않는다!
                # User가 바뀌게 되면 일일이 찾아서 수정해야 하고 
                # get_user_model 사용하면 활성화된 user를 알아서 찾아서 수정해준다. 


# User모델을 직접참조를 하지 않는다 
