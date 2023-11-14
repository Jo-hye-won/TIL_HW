# BACK

[Django REST framework](https://www.django-rest-framework.org/#quickstart)

**장고프레임워크 설치후에**
```bash
$ pip freeze > requirements.txt
```

startproject 할 때 현재위치(.)에 잘 해주자 

**설계도 그리기**
```bash
$ python manage.py makemigrations
```
- 무슨 이름 설정가능하다???
- 추가적인 설정 찾아서 해보기 

**django seed**
```bash
$ pip install django-seed
```
> 더미  데이터
1. 설치하고 
2. freeze 하고
3. settings에 installed_apps => `'django_seed'` 추가해주기
4. `python manage.py seed posts --number=10` 으로 더미데이터 만들어주기 

### 서버에서 데이터 받아오는거 막는거 치우려면?
[django-cors-headers 4.3.0](https://pypi.org/project/django-cors-headers/)

```bash
$ pip install django-cors-headers
```

```jsx
// settings.py
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    % "django.middleware.common.CommonMiddleware", // 이거 위에 배치해야 한다는 말
    ...,
]

CORS_ALLOW_ALL_ORIGINS = True
```


# ================================================================
# FRONT

