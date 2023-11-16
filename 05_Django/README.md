# 시작하기 전에..

## 프로젝트 관리
- TIL, 학습하고 있는 각종 폴더, 관통 PJT
- git으로 관리하는 중
  - TIL/**/*.py....
  - git으로 관리 되지 않아야 할 목록
    - .gitignore : 가상환경 생성 (git으로 관리 X)


## 가상환경
- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경
- git으로 관리 안한다! -> .gitignore 필요하다 
![gitignore.io] https://www.toptal.com/developers/gitignore/api/python,django,windows,pycharm,visualstudiocode,vue,venv
- requirements.txt -> 해당 프로젝트를 위한 독립 환경 목록 구성


- local 작업할 때, 가상환경 안만드록, global에 django 설치하고 작업 진행하면, 매번 똑같은 환경에서 진행하는데 왜 필요할까?
- version업데이트 매우 빠른 속도로 이루어진다. 

### 가상환경 생성
```bash
# 항상 작업위치 확인하기!
# 파이썬아/ -m모듈 써서/ virtual enviroment모듈써서/ 
# venv 라는 폴더에 가상환경 만들어줘

$ python -m venv venv
```

### 가상환경 실행
```bash
$ ls {venv folder_name}/ 

$ source{folder_name}/Scripts/Activate (folder_name)
$ pip list
```

## Django 설치
```bash
$ pip install django
```

### 다른 작업 환경을 위한 설정
```bash
# 현재 pip 목록을 얼린다. 
$ pip freeze > requirements.txt

# requirements.txt 파일에 적힌 내용으로 설치 
$ pip install -r requirements.txt
```

### Django 프로젝트 생성
```bash
# Django 프로젝트
# offline 이름의 프로젝트 
# django야 프로젝트 시작할건데 offline이름으로 할거야
$ django-admin startproject offline
$ cd offline

# 현재 작업 위치에 프로젝트 생성
$ django-admin startproject offline .
```

### Django 서버 실행
```bash
# 파이썬으로 manage.py(프로젝트 관리자파일)을 실행시킬건데,
# 서버를 실행시키는 명령어 
$ python manage.py runserver
# 개발용 서버주소를 주어줄 것이다. 
```

### Django App 추가하기
```bash
# articles
$ python manage.py startapp articles
```
```bash
# settings.py
INSTALEED_APPS = []
```

### articles app의 메인 페이지 화면에 띄우기
1. client가 요청 보낼 경로 지정하기 -> url
  - from articles import views
  - path('articles/', views.index)

2. 특정 경로에 요청이 왔을 때, 그 요청에 적절한 처리 하기(함수) -> views.py
  ```bash
  def index(request):
    return render(request, 'index.html')
  ```
3. 적절한 처리 과정에서 templates(html)이 필요하다면 작성하기 -> templates/*.html
   - index.html => <body> <h1> Articles 앱의 메인 페이지입니다.</h1></body>
  
4. 작성된 template을 사용자에게 반환하기 -> views에 정의한 함수의 return
   
