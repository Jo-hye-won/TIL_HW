# 
$ python -m venv venv

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktopmaster)
$ source venv/Scripts/activate
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktopmaster)
$ pip install -r requirements.txt
Collecting asgiref==3.7.2
  Using cached asgiref-3.7.2-py3-none-a
Collecting certifi==2023.5.7
  Using cached certifi-2023.5.7-py3-non
Collecting charset-normalizer==3.1.0
  Downloading charset_normalizer-3.1.0-
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Collecting Django==4.2.2
  Using cached Django-4.2.2-py3-none-an
Collecting djangorestframework==3.14.0
  Downloading djangorestframework-3.14.
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Collecting idna==3.4
  Using cached idna-3.4-py3-none-any.wh
Collecting pytz==2023.3
  Downloading pytz-2023.3-py2.py3-none-
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Collecting requests==2.31.0
  Using cached requests-2.31.0-py3-none
Collecting sqlparse==0.4.4
  Using cached sqlparse-0.4.4-py3-none-
Collecting typing_extensions==4.7.1
  Using cached typing_extensions-4.7.1-
Collecting tzdata==2023.3
  Using cached tzdata-2023.3-py2.py3-no
Collecting urllib3==2.0.3
  Downloading urllib3-2.0.3-py3-none-an
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Installing collected packages: pytz, ur
charset-normalizer, certifi, requests, 
Successfully installed Django-4.2.2 asg.0 djangorestframework-3.14.0 idna-3.4 extensions-4.7.1 tzdata-2023.3 urllib3-
WARNING: You are using pip version 22.0
You should consider upgrading via the 'on-response-practice\venv\Scripts\pytho
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktopmaster)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles
Running migrations:
  Applying contenttypes.0001_initial...
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_a
  Applying admin.0003_logentry_add_acti
  Applying articles.0001_initial... OK
  Applying contenttypes.0002_remove_con
  Applying auth.0002_alter_permission_n
  Applying auth.0003_alter_user_email_m
  Applying auth.0004_alter_user_usernam
  Applying auth.0005_alter_user_last_lo
  Applying auth.0006_require_contenttyp
  Applying auth.0007_alter_validators_a
  Applying auth.0008_alter_user_usernam
  Applying auth.0009_alter_user_last_na
  Applying auth.0010_alter_group_name_m
  Applying auth.0011_update_proxy_permi
  Applying auth.0012_alter_user_first_n
  Applying sessions.0001_initial... OK
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktopmaster)
$ python manage.py loaddata articles.js
Installed 20 object(s) from 1 fixture(s
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktopmaster)
$ python manage.py runserver
Watching for file changes with StatRelo
Performing system checks...

System check identified no issues (0 si
October 18, 2023 - 09:42:18
Django version 4.2.2, using settings 'm
Starting development server at http://1
Quit the server with CTRL-BREAK.

C:\Users\SSAFY\Desktop\TIL_HW\05_Django
changed, reloading.
Watching for file changes with StatRelo
Performing system checks...

System check identified no issues (0 si
October 18, 2023 - 09:45:11
Django version 4.2.2, using settings 'm
Starting development server at http://1
Quit the server with CTRL-BREAK.

Not Found: /
[18/Oct/2023 09:45:43] "GET / HTTP/1.1"
Not Found: /favicon.ico
[18/Oct/2023 09:45:43] "GET /favicon.ic
[18/Oct/2023 09:45:57] "GET /api/v1/art
[18/Oct/2023 09:45:58] "GET /static/res
[18/Oct/2023 09:45:58] "GET /static/res
HTTP/1.1" 200 13632[18/Oct/2023 09:45:58] "GET /static/rest_framework/js/bootstrap.min.js HTTP/1.1" 200 39680        
T /static/rest_framework/css/default.css HTTP/1.1"s HTTP/1.1" 200 1152
[18/Oct/2023 09:45:58] "GET /static/rest_frameworkt_framework/js/jquery-3.5.1.min.js HTTP9476       /1.1" 200 89476                        t_framework
[18/Oct/2023 09:45:58] "GET /static/rest_framework/img/grid.png HTTP/1.1" 200 icles/ HTTP
1458
[18/Oct/2023 09:51:38] "GET /api/v1/articles/ HTTPicles/ HTTP/1.1" 200 5613
[18/Oct/2023 09:52:46] "GET /api/v1/articles/ HTTPicles/ HTTP/1.1" 200 5613
[18/Oct/2023 09:52:52] "GET /api/v1/articles/ HTTPicles/ HTTP/1.1" 200 5613
[18/Oct/2023 09:53:02] "GET /api/v1/articles/ HTTPicles/ HTTP/1.1" 200 5613
[18/Oct/2023 09:53:11] "GET /api/v1/articles/ HTTP/1.1" 200 5613




#==========================


$ python python-request-sample.py
<class 'list'>
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/1018/99-json-response-practice (master)
$ python python-request-sample.py
[{'content': 'Bill third easy employee outside. Cup international bring '   
             'quality.\n'
             'Relate success degree. Indeed choose actually threat quite '  
             'partner friend. Important sort bring start space blood present.',
  'created_at': '2015-02-23T05:35:10Z',
  'id': 1,
  'title': 'Land probably you.',      
  'updated_at': '2010-08-05T01:26:46Z'},
 {'content': 'Speak final west. Forget manage lawyer to story sense.\n'     
             'Hotel natural blue soldier ready record either home. Information '
             'particularly either administration.',
  'created_at': '2000-04-26T10:44:04Z',
  'id': 2,
  'title': 'Economic probably must.', 
  'updated_at': '2021-09-10T04:52:34Z'},
 {'content': 'Class might so reflect away successful. Cell do industry '    
             'physical possible each. 
Management outside sell move network '             'suffer.\n'
             'Door education better fight interest choose lay. Me huge me upon '
             'across.',
  'created_at': '2001-05-13T15:29:50Z',
  'id': 3,
  'title': 'Sister wind page hour both some.',
  'updated_at': '1974-06-05T21:45:13Z'},
 {'content': 'Be artist sense. Course 
film tough remain loss risk begin. '  
             'Direction large matter such center.\n'
             'Machine purpose career house personal. Land ok represent than. '
             'Between weight idea stuff little.',
  'created_at': '1988-07-26T08:01:47Z',
  'id': 4,
  'title': 'Style strategy school gas 
two investment college.',
  'updated_at': '2010-09-09T22:31:27Z'},
 {'content': 'Interview according weight financial into agreement phone. Art '
             'seven court authority. Particular real wear anything develop '             'run.',
  'created_at': '1981-06-07T07:13:56Z',
  'id': 5,
  'title': 'Make although environmental during upon beat.',
  'updated_at': '1973-02-27T19:14:07Z'},
 {'content': 'Speech that note play.\n'
             'Or guy lose practice. Through will grow word. In what start can '
             'affect beyond capital.\n'
             'Idea large often fly your assume. Likely article policy friend.',
  'created_at': '1999-12-30T21:30:21Z',
  'id': 6,
  'title': 'Effect remain size brother town fill reveal.',
  'updated_at': '2014-07-17T19:50:11Z'},
 {'content': 'Drug sit wide end support not. Market war old book eye design 
'
             'do. Future scene marriage year citizen.',
  'created_at': '2000-06-18T15:09:41Z',
  'id': 7,
  'title': 'Out fill owner friend down never push born.',
  'updated_at': '1972-03-28T17:48:16Z'},
 {'content': 'Why away action individual. Nearly professional light student.\n'
             'Plant political education manager nation.\n'
             'Democratic trial discover stop those vote.',
  'created_at': '2002-07-02T10:49:50Z',
  'id': 8,
  'title': 'Brother until movie dinner rule world when decision.',
  'updated_at': '2016-11-08T05:22:49Z'},
 {'content': 'Stay operation glass. Seven Mr national parent.\n'
             'Beat put turn speech growth kid bag teach. Use season player '             'serious.',
  'created_at': '2002-03-03T13:36:24Z',
  'id': 9,
  'title': 'Use member recognize trouble whole.',
  'updated_at': '1983-11-04T02:37:09Z'},
 {'content': 'Certainly economy management task receive need body. Into '   
             'possible shoulder politics office subject increase easy. Until '
             'later win huge vote attack industry.',
  'created_at': '1999-03-20T07:13:58Z',
  'id': 10,
  'title': 'Time save improve long.', 
  'updated_at': '2000-11-09T15:46:14Z'},
 {'content': 'Usually pretty produce parent plant eight hear. Shake recognize '
             'art Mrs best wish religious chair. Per fear member maybe '    
             'environment sound student ahead.',
  'created_at': '2010-09-22T20:55:31Z',
  'id': 11,
  'title': 'Manage capital free personal suggest spring.',
  'updated_at': '1980-08-14T08:53:31Z'},
 {'content': 'Dark lay either others. 
Truth truth management ball she. World '
             'probably far product.', 
  'created_at': '1991-09-23T09:28:33Z',
  'id': 12,
  'title': 'Become sea tonight old bad far democratic.',
  'updated_at': '1978-08-29T02:51:49Z'},
 {'content': 'Drop stand yard difficult. Defense of half.\n'
             'Pull discuss me between. Performance admit keep also final oil '
             'style. Provide stay sound loss effort analysis attorney.',    
  'created_at': '2006-11-23T05:53:43Z',
  'id': 13,
  'title': 'Short himself life shake next goal.',
  'updated_at': '1972-12-08T01:16:35Z'},
 {'content': 'Physical word prove. Population would though law TV. Threat ' 
             'democratic including person board television human.\n'        
             'Eat while management contain. Air trip should according during '
             'east.',
  'created_at': '2016-05-04T20:43:49Z',
  'id': 14,
  'title': 'Skill yet suggest well wall back.',
  'updated_at': '1987-04-19T14:24:33Z'},
 {'content': 'Education avoid make including many process. Dinner consumer '             'surface sometimes carry. Idea order federal hear indeed save '             'run.',
  'created_at': '2008-10-08T13:35:06Z',
  'id': 15,
  'title': 'So minute so wish already.',
  'updated_at': '1989-09-05T08:18:26Z'},
 {'content': 'Blue although over these. Before exactly collection recognize 
'
             'specific upon something.',
  'created_at': '2010-04-15T09:17:47Z',
  'id': 16,
  'title': 'Ten hospital south house ago.',
  'updated_at': '1982-07-11T14:52:23Z'},
 {'content': 'Doctor guess standard school care who. Position school final '             'single. White gas ground season six option success.',
  'created_at': '2010-04-19T09:32:37Z',
  'id': 17,
  'title': 'Data measure camera right 
north feeling activity.',
  'updated_at': '1981-08-13T23:39:33Z'},
 {'content': 'Everyone dog job blood. 
Special establish southern apply. '   
             'Language place through professor she head type.',
  'created_at': '1983-02-22T00:59:49Z',
  'id': 18,
  'title': 'Idea main instead after.',  'updated_at': '1999-01-12T06:41:47Z'},
 {'content': 'Them success less money 
believe place. Left feeling eat race '             'care red. Door score yeah difference win human.',
  'created_at': '2017-03-25T16:15:53Z',
  'id': 19,
  'title': 'Gun lay hotel capital surface kitchen.',
  'updated_at': '1986-05-14T06:50:49Z'},
 {'content': 'Course arm follow conference board apply talk. See city student '
             'least. Performance bar available cultural member.',
  'created_at': '2021-09-10T02:14:16Z',
  'id': 20,
  'title': 'Dog treatment level.',    
  'updated_at': '1996-06-11T00:14:28Z'}]
(venv) 
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/1018/99-json-response-practice (master)
$ python python-request-sample.py
{'content': 'Bill third easy employee 
outside. Cup international bring '    
            'quality.\n'
            'Relate success degree. Indeed choosdeed choose actually threat quite '   
            'partner friend. Important sort brin sort bring start space blood present.',                                     'id': 1, 
 'created_at': '2015-02-23T05:35:10Z', 'id': 1,                             (venv)    
 'title': 'Land probably you.',       p/TIL_HW/0
 'updated_at': '2010-08-05T01:26:46Z'}e (master)(venv)
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/1018/99-json-response-practice (master)
$ python python-request-sample.py     p/TIL_HW/0
'Land probably you.'                  e (master)
(venv)
SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/TIL_HW/05_Django/1018/99-json-response-practice (master)
$





