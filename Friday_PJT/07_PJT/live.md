# 날씨 데이터를 활용한 REST API Server 구축
1. URL 식별자만 표시하자 (create 이런거 쓰지말자)
2. HTTP Method 로 표기하자!

## 무슨 서버를 구축할까?
- 클라이언트에게 날씨 정보를 제공해주는 서버를 구축합니다.
- 우리는 날씨 정보 원본 데이터를 OpenWeatherMap API를 통해 가져올 것입니다.

- DRF 화면이나 포스트맨으로 확인하기
- GET/ POST / DELETE /UPDATE

### 백엔드 개발
- REST API 서버 개발 <- 이번 프로젝트 목표

### 프론트엔드 개발
- REST API를 사용하여, 결과를 받아 화면 구성

> Django로 백엔드를 개발하고, 차후 Vue.js를 학습하여 프론트엔드를 개발하여 하나의 완성된 웹 Application을 개발 할 예정



startapp weathers => settings.py에  'weathers', 'rest_framework', 등록하기