'''
$ python -m venv venv

$ source venv/Scripts/Activate

$ pip install django ipython django-extensions

$ pip freeze > requirements.txt

$ django-admin startproject crud .

$ python manage.py runserver

$ python manage.py startapp articles

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py createsuperuser

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