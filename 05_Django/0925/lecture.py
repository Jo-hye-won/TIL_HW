'''
$ python -m venv vnev

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python -m venv venv

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ source venv/Scripts/Activate
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ pip install django ipython django-extensions
Collecting django
  Using cached Django-4.2.5-py3-none-any.whl (8.0 MB)
Collecting ipython
  Using cached ipython-8.15.0-py3-none-any.whl (806 kB)
Collecting django-extensions
  Using cached django_extensions-3.2.3-py3-none-any.whl (229 kB)
Collecting tzdata
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting asgiref<4,>=3.6.0
  Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting matplotlib-inline
  Using cached matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
Collecting stack-data
  Using cached stack_data-0.6.2-py3-none-any.whl (24 kB)
Collecting jedi>=0.16
  Using cached jedi-0.19.0-py2.py3-none-any.whl (1.6 MB)
Collecting backcall
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting pickleshare
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30
  Using cached prompt_toolkit-3.0.39-py3-none-any.whl (385 kB)
Collecting pygments>=2.4.0
  Using cached Pygments-2.16.1-py3-none-any.whl (1.2 MB)
Collecting traitlets>=5
  Using cached traitlets-5.10.0-py3-none-any.whl (120 kB)
Collecting decorator
  Using cached decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting exceptiongroup
  Using cached exceptiongroup-1.1.3-py3-none-any.whl (14 kB)
Collecting typing-extensions
  Downloading typing_extensions-4.8.0-py3-none-any.whl (31 kB)
Collecting parso<0.9.0,>=0.8.3
  Using cached parso-0.8.3-py2.py3-none-any.whl (100 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.6-py2.py3-none-any.whl (29 kB)
Collecting executing>=1.2.0
  Using cached executing-1.2.0-py2.py3-none-any.whl (24 kB)
Collecting pure-eval
  Using cached pure_eval-0.2.2-py3-none-any.whl (11 kB)
Collecting asttokens>=2.1.0
  Using cached asttokens-2.4.0-py2.py3-none-any.whl (27 kB)
Collecting six>=1.12.0
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: wcwidth, pure-eval, pickleshare, executing, backcall, tzdata, typing-extensions, traitlets, sqlparse, six, pygments, prompt-toolkit, parso, exceptiongroup, decorator, colorama, matplotlib-inline, jedi, asttokens, asgiref, stack-data, django, ipython, django-extensions
Successfully installed asgiref-3.7.2 asttokens-2.4.0 backcall-0.2.0 colorama-0.4.6 decorator-5.1.1 django-4.2.5 django-extensions-3.2.3 exceptiongroup-1.1.3 executing-1.2.0 ipython-8.15.0 jedi-0.19.0 matplotlib-inline-0.1.6 parso-0.8.3 pickleshare-0.7.5 prompt-toolkit-3.0.39 pure-eval-0.2.2 pygments-2.16.1 six-1.16.0 sqlparse-0.4.4 stack-data-0.6.2 traitlets-5.10.0 typing-extensions-4.8.0 tzdata-2023.3 wcwidth-0.2.6
WARNING: You are using pip version 22.0.4; however, version 23.2.1 is available.
You should consider upgrading via the 'C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\Scripts\python.exe -m pip install --upgrade pip' command.
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ pip freeze > requirements.txt
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ django-admin startproject crud .
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ ls
crud/  exam/  manage.py*  README.md  requirements.txt  venv/
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 25, 2023 - 12:12:16
Django version 4.2.5, using settings 'crud.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[25/Sep/2023 12:12:30] "GET / HTTP/1.1" 200 10664
Not Found: /favicon.ico
[25/Sep/2023 12:12:31] "GET /favicon.ico HTTP/1.1" 404 2108

(venv)
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python manage.py startapp articles
(venv)
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python manage.py makemigrations
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Articles
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python manage.py createsuperuser
Username (leave blank to use 'ssafy'): admin
Email address: 
Password: 
Password (again):
Error: Your passwords didn't match.
Password: 
Password (again):
Error: Your passwords didn't match.
Password: 
Password (again):
Error: Your passwords didn't match.
Password: 
Password (again):
Error: Your passwords didn't match.
Password: 
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/0925 (master)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 25, 2023 - 12:27:29
Django version 4.2.5, using settings 'crud.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[25/Sep/2023 12:27:31] "GET / HTTP/1.1" 200 10664
[25/Sep/2023 12:27:42] "GET / HTTP/1.1" 200 10664
[25/Sep/2023 12:29:12] "GET /admin/ HTTP/1.1" 302 0
[25/Sep/2023 12:29:12] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4181
[25/Sep/2023 12:29:13] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2694
[25/Sep/2023 12:29:13] "GET /static/admin/css/base.css HTTP/1.1" 200 21207
[25/Sep/2023 12:29:13] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2929
[25/Sep/2023 12:29:13] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18533
[25/Sep/2023 12:29:13] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[25/Sep/2023 12:29:13] "GET /static/admin/css/login.css HTTP/1.1" 200 958
[25/Sep/2023 12:29:13] "GET /static/admin/js/theme.js HTTP/1.1" 200 1943
[25/Sep/2023 12:29:17] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[25/Sep/2023 12:29:17] "GET /admin/ HTTP/1.1" 200 6228
[25/Sep/2023 12:29:17] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[25/Sep/2023 12:29:17] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[25/Sep/2023 12:29:17] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[25/Sep/2023 12:29:37] "GET /admin/articles/articles/add/ HTTP/1.1" 200 8901
[25/Sep/2023 12:29:37] "GET /static/admin/css/forms.css HTTP/1.1" 200 9047
[25/Sep/2023 12:29:37] "GET /static/admin/js/actions.js HTTP/1.1" 200 7872
[25/Sep/2023 12:29:37] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[25/Sep/2023 12:29:37] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 8943
[25/Sep/2023 12:29:37] "GET /static/admin/js/core.js HTTP/1.1" 200 5682
[25/Sep/2023 12:29:37] "GET /admin/jsi18n/ HTTP/1.1" 200 3343
[25/Sep/2023 12:29:37] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11900
[25/Sep/2023 12:29:37] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[25/Sep/2023 12:29:37] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7887
[25/Sep/2023 12:29:37] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 586
[25/Sep/2023 12:29:37] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 292458
[25/Sep/2023 12:29:37] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[25/Sep/2023 12:29:37] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[25/Sep/2023 12:30:11] "POST /admin/articles/articles/add/ HTTP/1.1" 302 0
[25/Sep/2023 12:30:12] "GET /admin/articles/articles/ HTTP/1.1" 200 8871
[25/Sep/2023 12:30:12] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6566
[25/Sep/2023 12:30:12] "GET /admin/jsi18n/ HTTP/1.1" 200 3343
[25/Sep/2023 12:30:12] "GET /static/admin/js/filters.js HTTP/1.1" 200 978
[25/Sep/2023 12:30:12] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[25/Sep/2023 12:30:12] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[25/Sep/2023 12:31:36] "GET /admin/articles/articles/add/ HTTP/1.1" 200 8901
[25/Sep/2023 12:31:36] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[25/Sep/2023 12:31:36] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[25/Sep/2023 12:31:36] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[25/Sep/2023 12:31:36] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[25/Sep/2023 12:31:36] "GET /static/admin/js/theme.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:36] "GET /admin/jsi18n/ HTTP/1.1" 200 3343
[25/Sep/2023 12:31:36] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "POST /admin/articles/articles/add/ HTTP/1.1" 302 0
[25/Sep/2023 12:31:43] "GET /admin/articles/articles/ HTTP/1.1" 200 9095
[25/Sep/2023 12:31:43] "GET /static/admin/js/jquery.init.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/actions.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/core.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/prepopulate.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /static/admin/js/urlify.js HTTP/1.1" 304 0
[25/Sep/2023 12:31:43] "GET /admin/jsi18n/ HTTP/1.1" 200 3343
C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\crud\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\threading.py", line 980, in _bootstrap_inner
    self.run()
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\threading.py", line 917, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\management\base.py", line 485, in check
    all_issues = checks.run_checks(
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\resolvers.py", line 494, in check
    for pattern in self.url_patterns:
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\utils\functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\resolvers.py", line 715, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\utils\functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\resolvers.py", line 708, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\crud\urls.py", line 22, in <module>
    path('articles/', include('articles.urls'))
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\conf.py", line 38, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'articles.urls'
C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\articles\admin.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\threading.py", line 980, in _bootstrap_inner
    self.run()
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\threading.py", line 917, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\management\base.py", line 485, in check
    all_issues = checks.run_checks(
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\resolvers.py", line 494, in check
    for pattern in self.url_patterns:
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\utils\functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\resolvers.py", line 715, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\utils\functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\resolvers.py", line 708, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\SSAFY\AppData\Local\Programs\Python\Python39\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\crud\urls.py", line 22, in <module>
    path('articles/', include('articles.urls'))
  File "C:\Users\SSAFY\Desktop\TIL_HW\05_Django\0925\venv\lib\site-packages\django\urls\conf.py", line 38, in include
    urlconf_module = import_module(urlconf_module)
rt                                                             ib\importlib\__init__.py", line 127, in import_module
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load                                                          rt
  File "<frozen importlib._bootstrap>", line 984, in _find_and__loadload_unlocked                                                  load_unlocked
ModuleNotFoundError: No module named 'articles.urls'
'''