Form class 정의
widgets = HTML의 iput element의 표현을 담당

# Django Form 
- HTML 'form' 
  : 지금까지 사용자로부터 데이터를 받기 위해 활용한 방법
    그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
  -> 유효한 데이터인지에 대한 확인이 필요
  
## 유효성 검사 
> 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검사 구현
    - 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등
    많은 것들을 고려해야 함
    - 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용
    

# Django ModelForm
- Form : 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)
- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글, 회원가입)


- is_valid() : 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

# Handling HTTP requests
## new & create view 함수간 공통점과 차이점
- 공통점 : 데이터 생성을 구현하기 위함(목적 -> 게시글 생성)
- 차이점 : new 는 GET method 요청만을, create는 POST method 요청만을 처리
