from django.contrib.auth.forms import UserCreationForm

# model 선택 세 가지 방법
# 1. 직접 가져오기 -> 권장 X
# from . models import User

# 2. settings에 설정된 모델 가져오기
# from django.conf import settings # model = settings.AUTH_USER_MODEL
# -> 문자열 -> models.py에 작성할 때는 문자열로 적는 게 좋다!

# 3. get_user_model 메서드 활용
from django.contrib.auth import get_user_model



class CustomUserCreationFrom(UserCreationForm):
    # class Meta(UserCreationForm.Meta):
    class Meta:
        # model = 나의 User 모델
        model = get_user_model() 
        fields = UserCreationForm.Meta.fields
        
        # fields = '__all__' 
        # 이거 없으면 accounts is not registerd ~ 등록된 네임스페이스가 아니에요!
