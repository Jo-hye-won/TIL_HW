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


6. form 태그 닫히는 구문 어디있는지 잘 확인하자!
```html
  <form action="{% url "accounts:login" %}" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value='로그인'> 
    </form>
```
여기에서 form태그 닫히는게 젤 위페이지에 있었어서 오류가 생겼다.

7. book_pk와 book.pk의 차이
- url => 문자열로 변수명을 book_pk로 지정 하겠다는 것
- html=> book.pk는 book 객체가 가진 pk 속성을 부르기 위해 dot notation으로 접근 한 것 ex) person.name

8. redirect함수가 하는 일 
- 인자로 넘겨 받은 문자열을 app_name : pattern_name으로 사용해서
적절한 경로 명(urls.py 에 작성한 이름)으로 GET요청을 보내는 것