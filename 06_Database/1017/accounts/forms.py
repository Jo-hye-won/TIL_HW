from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
# 유저 생성을 위한 Form이 이미 있는데... 바꿔서 써야 하는 이유...?
# 기본 제공 UserCreationForm은 model 을  auth.User를 쓰고 있음
# 우리는 accounts.User를 쓸거임
class CustomUserCreationForm(UserCreationForm):
    # Meta class는 왜 상속받아서 쓰나요?
    # 우리는 Meta class에서 model, field, exclude 정도 쓰고 있는데...
    class Meta(UserCreationForm.Meta):
        model = User