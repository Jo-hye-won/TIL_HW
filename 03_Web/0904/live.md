## Web
- World Wide Web : 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
- Web : Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
- Web site : 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
- Web page : HTML, CSS 등의 웹 기술을 이용하여 만들어진 "Web site"를 구성하는 하나의 요소

### Web page구성요소
- HTML : 구조
- CSS : 스타일링
- Javascript : 행동

## 웹 구조화

## HTML(HyperText Markup Language)
> 웹 페이지의 의미와 '구조'를 정의하는 언어
: 프로그래밍 언어가 아니라 마크업 언어
: 프로그래밍 언어가 되기위한 조건 충족 X : 연산, 반복문 X
* Hypertext : 웹 페이지를 다른 페이지로 연결하는 링크
  : 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
* Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 
  ex. HTML. Markdown


## Structure of HTML
- <!DOCTYPE html> : 해당 문서가 html로 문서라는 것을 나타냄
- <html></html> : 전체 페이지의 콘텐츠를 포함
 : 슬래시 없는거 = 열린 태그 / 슬래시 있는거 = 닫힌 태그 
 : 태그들 사이에서 상하관계가 존재함
 : lang="en" : 언어 = 영어
- <meta charset="UTF-8"> : 닫는 태그가 없음
   (닫는 태그가 있다는 건-> 내용이 들어간다는것)
- <p> paragraph 문단을 뜻한다
- alt + b 누르면 페이지 렌더링해서 나온다. 
-  <title> My page  </title> 
 : 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- <head></head> : HTML 문서에 관련된 설명, 설정 등
        : 사용자에게 보이지 않음
- <body></body> : 페이지에 표시되는 모든 콘텐츠

-  <a href="https://www.google.co.kr/">Google</a> : 하이퍼 텍스트 만드는 a태그


### HTML Element(요소) - memo
- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재 

### HTML Attributes(속성)
1. 규칙
- 속성은 요소 이름과 속성 사이에 공백이 있어야 함
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
- 속성값은 열고 닫는 따옴표로 감싸야 함(작은따옴표 상관없지만 쓰지 않습니다)

2. 목적
- 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
- CSS 에서 해당 요소를 선택하기 위한 값으로 활용됨
- <a href="https://www.google.co.kr/" <= 요기가 속성
   -> 본인의 영역만큼만 자리를 차지함
- <img src="images/sample.png" alt="sample-img">
  : 이미지파일 경로             alt = 이미지파일 오류 있을때의 대체 이미지


  ### HTML Text structure
  - HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것
  - HTML : 웹 페이지의 의미와 구조를 정의하는 언어
  - <h1> Heading</h1> : 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것
  > ! + tab 하면 기본구조 나옴!!!!


  #### 대표적인 HTML Text sturcture
  - heading & Paragraphs : h1~6, p
  - Lists : ol, ul, li
  - Emphasis & Importance : em, strong

- <em> emphasis </em> : 기울임
-  <ol> = 정렬된 리스트 (ordered list)
    <li> 파이썬 </li> = 리스트 목록
    <li> 알고리즘</li>
    <li> 웹</li>
  </ol>
- <ol>을 <ul> 로 바꾸면 블립(?)모양으로 바뀜 
- <em> 강조.이테릭체
- <strong> 강조

> html은 들여쓰기 안해도 아무 이상 없지만 구조 잘 보기 위해서 들여쓰기함
  두칸 들여쓰기 권장!
  문법 잘못되었다고 알려주지 않음 ㅠ -> 디버깅하기 골치 아플 수 있음 


# 웹 스타일링
## CSS (Cascading Style Sheet)
> 웹 페이지의 디자인과 레이아웃을 구성하는 언어 

### CSS구문
h1(선택자_Selector) {
  color: red;
  font-size(속성): 30px(값); 
  => 속성(Property)과 값(Value)을 하나의 선언(Declaration)이라고 함 (;으로 한줄 한줄 선언을 명시해줘야함)
}

### CSS 적용방법
1. 인라인(inline) 스타일 
    : HTML 요소 안에 style 속성 값으로 작성
    : 제일 권장하지 않음 : HTML이 구조를 보기 위함인데 이렇게 하면 잘 안보임

2. 내부(internal) 스타일 시트 
    : head 태그 안에 style 태그에 작성
    : 수업은 2번 방식으로 

3. 외부(external) 스타일 시트 
    : 별도의 CSS 파일 생성 THML 태그를 사용해 불러오기
    : 요 스타일을권장함 : 재사용성 때문에 


### CSS Selectors 
> HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
1. 기본 선택자
 - 전체 선택자(*) : HTML 모든 요소를 선택
 - 요소 선택자 : 지정한 모든 태그를 선택 
 - 클래스 선택자 : '.' : 주어진 클래스 속성을 가진 모든 요소를 선택
 - 아이디 선택자 : '#' : 주어진 아이디 속성을 가진 요소 선택
                      : 문서에는 주어진 아이디를 가진 요소가 '하나만' 있어야 함
 - 속성 선택자 등

2. 결합자(Combinators)
 - 자손 결합자
  : 첫 번째 요소의 자손 요소들 선택
  : p.span은 <p> 안에 있는 모든 <span>를 선택(하위 레벨 상관 없이)
  
 - 자식 결합자
  : 첫 번째 요소의 직계 자식만 선택
  : ul > li  은 <ul> 안에 있는 모든 <li>를 선택(한단계 아래 자식들만)

> 결합자: 공백 = 자손들 / '>' 는 자식만

### 우선순위
> Cascade(계단식) : 동일한 우선순위를 같은 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용됨 
1. !important : 다른 우선순위 규칙보다 우선하여 적용하는 키워드
  : Cascade 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하진 않음

2. inline 스타일
3. 선택자 - id선택자 > class 선택자 > 요소 선택자
4. 소스 코드 순서 순으로 우선순위가 높다

### CSS 상속
: 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
- 상속 여부 
1. 상속 되는 속성
 : Text 관련 요소 (font, color, text-align, opacity, visibility 등)

2. 상속 되지 않는 속성
 : Box model 관련 요소(width, height, border, box-sizing)
 : position 관련 요소(position, top/right/bottom/left,z-index) 등

[web docs] (how to render image in html mdn)
