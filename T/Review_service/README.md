1. from django.contrib.auth.models import AbstractUser 받아올때 
auth. 뒤에 models 안하면 AbstractUser 안불러와짐


2. settings.py :  AUTH_USER_MODELS = 'accounts.user' 이 아니라 
                  AUTH_USER_MODEL = 'accounts.User'


3.   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 할 때,
     models. 해줘야 뒤에 CASCADE 나온다. 고냥 CASCADE 해주려고 했음.
     settings.AUTH_USER_MODEL => 세팅스의 AUTH_USER_MODEL을 참조한다. 


4. admin site에 모델이 출력되게 하기 위해서는 
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```
이렇게 등록 먼저 해주고 나서 makemigrations 또는 migrate 진행해야 한다 !

5.  return render(reqest, 'libraries:detail.html', context)
 => 경로 'libraries:detail.html' 이렇게 하면 안돼
        'libraries/detail.html' 이케 해야 함
