- ul.nav.>li.nav-item*4>a{메뉴 $}: 한단계아래에 자식리스트 만들건데 4개를 만들겠다 그안에 a테그만들건데 컨텐츠는 메뉴를 넣을거당 메뉴는 1부터 카운팅이되는 숫자를 가져간다

- emmet
[emmet]https://docs.emmet.io/cheat-sheet/

# Bootstrap Grid system
> 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
- Grid system 목적 : 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

## Grid system 기본요소
1. Container : Cloumn들을 담고 있는 공간
2. Column : 실제 컨텐츠를 포함하는 부분
3. Gutter : 컬럼과 컬럼 사이의 여백 영역

- 1개의 row안에 12칸의 column 영역이 구성 -> 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨 (+ 화면 크기 별)


###  Responsive Web Design
> 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
- Bootstrap grid system에서는 12개 column과 6개 breakpoints를 사용하여 반응형 웹 디자인을 구현

### Grid system breakpoints
> 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
- 높이가 아니라 화면 너비에 따라 6개의 분기점 제공(xs, sm ,md, lg, xl, xxl)
- 각 breakpoints 마다 설정된 최대 너비 값 '이상으로' 화면이 켜지면 grid system 동작이 변경됨
