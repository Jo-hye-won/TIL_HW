## Bootstrap 
> CSS 프론트엔드 프레임워크(Toolkit)
- 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

### 기본 사용법
     m       t   -  5
{property}{sides}-{size}

<property>
m = margin
p = padding

<sides>
t = top
b = bottom
left = s (start)
right = e (end)
y = top, bottom
x = left, right
blank = 4방면 모두 

<size>
0 = 0 rem(rem = 16px을 곱해준 것) = 0px
1 = 0.25 rem = 4px
2 = 0.5 rem = 8px
3 = 1 rem = 16px
4 = 1.5 rem = 24px
5 = 3 rem = 48px
auto

## Typography
> 제목, 본문 텍스트, 목록 등

1. Display headings
: 기존 Heading보다 더 눈에 띄는 제목이 필요할 경우
  (더 크고 약간 다른 스타일)

2. Inline text elements
3. Lists


.text-* => *에 색이름이 들어간다 

## Component 
> bootstrap에서 제공하는 UI 관련 요소
 - 버튼, 네비게이션 바, 카드, 폼, 드롭다운 등
 - 이점 : 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용


### Semantic Web 
> 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식
- 이 요소가 가진 목적과 역할은 무엇일까?

### HTML Semantic Element
:  검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록
   기본적인 모양과 기능 이외에 의미를 가지는 HTML요소
   
### Semantic in CSS
- OOCSS : 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론
- CSS 방법론 : CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

#### OOCSS 기본원칙
1. 구조나 스킨을 분리
 - 구조와 스킨을 분리함으로써 재사용 가능성을 높임
 - 모든 버튼의 공통구조를 정의 + 각각의 스킨(배경색과 폰트 색상)을 정의

2. 컨테이너와 콘텐츠를 분리
 - 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용
 - 스타일을 정의할 때 위치에 의존적인 스타일을 사용하지 않도록 함
 - 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지 

 -.header와 .footer 클래스가 폰트 크기와 색 둘 다 영향을 줌.
  - .container .title이 폰트 크기 담당(콘텐츠 스타일)
  - .header와 .footer가 폰트 색 담당(컨테이너 스타일)

  ### CDN : Content Delivery Network
   - 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
   - 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화(웹 페이지 로드 속도를 높임)
   - 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달
