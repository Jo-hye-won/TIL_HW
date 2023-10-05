# 회원 가입
- User 객체를 Create 하는 과정

## UserCreationForm()
- 회원 가입시 사용자 입력 데이터를 받을 built-in ModelForm

- 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 Form
### UserCreationForm
### get_user_model() 
: 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수

> User모델을 직접참조하지 않는 이유
- get_user_mode()을 사용해 User모델을 참조하면 커스텀 User모델을 자동으로 반환해주기 대문
- Django 는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 필수적으로 강조하고 있음
-> User model 참조에 대한 자세한 내용은 추후 모델 관계에서 다룰 예정




### UserChangeForm



# 회원 탈퇴
- User 객체를 Delete 하는 과정

# 회원정보 수정
# 비밀번호 변경
# 로그인 사용자에 대한 접근 제한
