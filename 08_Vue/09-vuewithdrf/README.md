## makemigrations
- 할때 기존 설계도 안지우고 하면 덮어쓸건지 물어본다
> It is impossible to add a non-nullable field 'user' to article without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with 
a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 1

- 그러면 ` 1 ` ` 1 ` 하고 덮어쓰면 된당!!


### Dj-Rest_Auth
- 회원가입, 인증(소셜미디어 인증 포함)
- 등록기능 추가 설정

토큰을 같이 보내야 인증할 수 있음
- key 이름이 authorization으로 정해져 있음  여기다가 
`Token 토큰주소`로 입력해줘야 한다. Token하고 한자리 띄워야한다. 


# -------------------------------------------------------------
## 권한 정책 설정
