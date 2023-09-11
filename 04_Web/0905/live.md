## CSS Layout
### CSS Box Model
> 모든 HTML 요소를 사각형 박스로 표현하는 개념
- 내용(content) : 콘텐츠가 표시되는 영역
- 안쪽 여백(Padding) : 콘텐츠 주위에 위치하는 공백 영역
- 테두리(Border) : 콘텐츠와 패딩을 감싸는 테두리 영역
- 외부 간격(Margin) : 박스와 외부요소 사이의 간격
    으로 구성되는 개념


> margin-left: auto; : 오른쪽 정렬 됨    

> margin-left: auto;
  margin-right: auto;  
     => 양쪽 다 나눠주면서 가운데 정렬이 된다. 


#### width & height 속성
- 요소의 너비와 높이를 지정 : 이때 지정되는 요소의 너비와 높이는 콘텐츠(content) 영역을 대상으로 함

### 박스 타입
- Block & Inline
- Normal flow 
 : CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향
- block은 옆에 자리 다 차지함

1. Block 타입
- 항상 새로운 행으로 나뉨
- width 와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
- 기본적으로 width 속성을 지정하지 않으면 박스는 inline방향으로 사용가능한 공간을
  모두 차지함(너비를 사용가능한 공간의 100%로 채우는 것)
- 대표적인 bolck타입 태그 : h1~6 / p / div
- margin으로 수평정렬

2. Inline 타입
- 새로운 행으로 나뉘지 않음
- 컨텐츠의 크기에 따라서 높이와 너비가 정해지기 때문에 width와 height 속성을 사용할 수 없음 ★★
- 수직방향으로 padding, margins, borders가 적용되지만 
  다른 요소를 밀어낼 수는 없음
- 수평방향 : padding,  margins, borders가 적용되어
  다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그 : a(링크), img(이미지), span
- align으로 수평정렬


## 기타 display 속성
### inline-block
- inline과 block 요소 사이의 중간 지점을 제공하는 display값
- block 요소의 특징을 가짐
  - width 및 height 속성 사용 가능
  - padding, margin 및 border로 인해 다른 요소가 밀려남
- 요소가 줄 바꿈 되는 것을 원하지 않으면서(inline의 속성) 너비와 높이를 적용하고 싶은 경우에 사용(block의 속성)

### None
> 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음 

## CSS Layout Position
> CSS Layout은 각 요소의 위치와 크기를 조정하여 웹페이지의 디자인을 결정하는 것 
  (Display, position, float, flexbox 등)
> CSS Position은 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
 : 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등

### Position 유형
1. Static 
- 기본값
- 요소를 Normal Flow에 따라 배치

2. Relative : 본인의 과거의 영역을 버리지 않음 
- 요소를 Normal Flow에 따라 배치
- 자기 자신을 기준으로 이동
- 요소가 차지하는 공간은 static일 때와 같음

3. Absolute : 집 나간 자식 : 본인의 영역을 버리고 떠남 
- 요소를 Normal Flow에서 제거
- 가장 가까운 relative 부모 요소를 기준으로 이동
- 문서에서 요소가 차지하는 공간이 없어짐
- 다른요소들이 이동하게 된다  
- 집나가는 기준 = static이 아닌 부모를 찾음

4. fixed : 얘도 집나간 자식
- 요소를 Normal Flow에서 제거
- 현재 화면영역(viewport)을 기준으로 이동
- 문서에서 요소가 차지하는 공간이 없어짐
- 브라우저를 기준으로 고정되어 있음 

5. Sticky 
- 요소를 Normal Flow에 따라 배치
- 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면
  그 위치에서 고정됨(fixed)
- 만약 다음 sticky 요소가 나오면 다음 sticky요소가 이전 sticky 요소의 자리를 대체
- 이전 sicky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 
  겹치게 되기 때문


## Z-index 
> 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
- 정수 값을 사용해 Z축 순서를 지정
- 더 큰 값을 가진 요소가 작은 값의 요소를 덮음


# ★ CSS Layout Flexbox ★
> 요소를 행과 열 형태로 배치하는 1차원(선) 레이아웃 방식
> '공간배열' & '정렬'

## 기본 사항
- Flex Container라는 부모가 자식요소들(Flex item)을 1차원으로 배열하고 정렬함
- 수평축이 메인 축이 됨(main axis)
- 수직으로 되어 있는 것을 교차 축이라고 함 (cross axis)
- 시작점 : 축기준으로 생각해야 함 (메인 축 기준으로) 
  왼쪽부터 시작해야 함(main start) 
  교차축의 시작점 - 위쪽(cross start) 
  => 기본값일 때다 !
  => 축의 시작점과 교차점은 바뀔 수 있음 !

1. main axis(주 축)
- flex ite들이 배치되는 기본 축
- main start에서 시작하여 main end방향으로 배치

2. cross axis(교차 축)
- main axis에 수직인 축
- cross start에서 시작하여 cross end 방향으로 배치
 
3. Flex Container : 배치된 애들을 감싸는 부모
- dispaly : felx; 혹은 display: inlin-flex; 가 설정된 부모 요소
- 이 컨테이너의 1차 자식요소들이 flex item이 됨
- flex container 는 한단계 아래의 요소들에 대해서만 역할을 하게 됨!!
- flexbox 속성 값들을 사용하여 자식 요소 flex item들을 배치 

4. Flex item
- Flex container 내부에 레이아웃 되는 항목

### 레이아웃 구성
1. flex Container 지정
2. flex-direction 지정
3. flex-wrap
4. justify-content
5. align-content
6. align-items
7. align-self
8. felx-grow
9. flex-basis


content = 여러행
