# SNS 서비스

### CR 기능 구현
- 요구 사항
1. gitignore를 포함하여야 한다.
2. 새로운 가상 환경을 생성하고, 가상 환경 내에서 django를 설치한다.
3. project 명은 inmoongram으로 생성한다.
4. app 명은 articles로 생성한다.
5. Article model을 정의한다.
    - 정의해야 할 필드 정보는 첨부 파일을 참고
    - 사용자가 업로드한 이미지를 저장할 수 있어야 한다.
        - 업로드 경로는 /media/ 로 설정 한다.
    - 이미지는 게시글 작성 시 생략되어도 생성 할 수 있도록 모델을 정의한다.
        - 첨부된 이미지가 존재하는 경우에만 이미지를 출력하도록 한다.
    - 공개 여부를 나타내는 is_public의 기본값을 True로 설정한다.
6. 게시글 전체 목록 조회 기능을 구현한다.
7. 게시글 생성 기능을 구현한다.
8. 게시글 상세 조회 기능을 구현한다.
9. base template을 사용하여 template을 상속받아야 한다.
10. 게시글 생성을 위한 html form은 django의 ModelForm을 사용하여 구현한다.

### 기본 이미지 기능
- 요구 사항
1. 사용자가 이미지를 업로드 하지 않은 경우, 제공된 기본 이미지가 나타나도록 설정한다.
    - DTL 조건문을 활용하여 구성한다.
    - 기본 이미지의 저장 위치는 프로젝트 최상위 폴더에서 'static/assets/' 위치에 저장한다.
    - 기본 이미지의 크기는 가로 300px 세로 300px을 넘지 않도록 설정한다.
2. '/static/assets/style.css/' 에 CSS 속성을 정의하여 모든 요소의 마진, 패딩의 값을 0이 되도록 설정한다.
3. style.css는 모든 template에 적용 될 수 있도록 base.html에서 불러온다.