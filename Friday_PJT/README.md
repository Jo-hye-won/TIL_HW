# 7/21 관통 PJT1 [파이썬을 이용한 데이터 수집]

**금융상품비교 / 영화추천서비스 중 선택**

(PJT4 시간까지는 변경 가능하나 5부터는 변경 불가)

- **파이썬으로 정기 예금 데이터 수집 및 미션 수행**
    - 외부 서버를 활용한 데이터 수집
    - 요구사항에 맞게 JSON 형태 데이터 가공
- **파이썬으로 도서 및 아티스트 데이터 가공 및 미션 수행**
    - 샘플 데이터 제공
    - 요구사항에 맞게  JSON 형태 데이터 가공

- **서버** : 부탁을 받으면 처리해주거나, 부탁대로 원하는 값을 돌려주는 역할을 함
- **클라이언트** : 부탁하는 역할

- 요청은 어떻게?
    - Python 라이브러리 requests 사용
```python
import requests

url = "http://fakestoreapi.com/carts" # 요청을 보내는 서버의 주소
data = requests.get(url) # 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수
print(data.json()) #.json() 내부의 데이터를 JSON(파이썬의 딕셔너리와 비슷함) 형태로 변환해주는 함수

"""출력결과
[{'id': 1, 'userId': 1, 'date': '2020-03-02T00:00:00.000Z', 'products': [{'productId': 1, 'quantity': 4}, {'produc
tId': 2, 'quantity': 1}, {'productId': 3, 'quantity': 6}], '__v': 0}, {'id': 2, 'userId': 1, 'date': '2020-01-02T0
0:00:00.000Z', 'products': [{'productId': 2, 'quantity': 4}, {'productId': 1, 'quantity': 10}, {'productId': 5, 'q
uantity': 2}], '__v': 0}, {'id': 3, 'userId': 2, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 1,
 'quantity': 2}, {'productId': 9, 'quantity': 1}], '__v': 0}, {'id': 4, 'userId': 3, 'date': '2020-01-01T00:00:00.
000Z', 'products': [{'productId': 1, 'quantity': 4}], '__v': 0}, {'id': 5, 'userId': 3, 'date': '2020-03-01T00:00:
00.000Z', 'products': [{'productId': 7, 'quantity': 1}, {'productId': 8, 'quantity': 1}], '__v': 0}, {'id': 6, 'us
erId': 4, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 10, 'quantity': 2}, {'productId': 12, 'qu
antity': 3}], '__v': 0}, {'id': 7, 'userId': 8, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 18,
 'quantity': 1}], '__v': 0}]
"""
```
    - 주소창에 주소(URL)을 입력
    [fakesotreapi.com](https://fakestoreapi.com/carts)


- **API** : 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램
    - 기능 예시: 데이터 저장, 조회, 수정, 삭제 등등
    - 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둠
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b45763e3-3ac6-4462-9d26-4ed954fb9f2f/Untitled.png)
    
    - 날씨 정보를 수집하기 위해서는 두 가지를 찾아야 함
        - 날씨 정보를 가지고 있는 서버
        - 해당 서버가 제공하는 API
    - **오픈API** : 외부에서 사용할 수 있도록 무료로 개방(OPEN)된 API
        - 오픈API 특징 및 주의 사항
            - 악성 사용자가 여러 계정으로 동시 요청을 보내면 서버가 마비됨 → API KEY를 발급받아 사용해야함
            - 한 계정에서 너무 많은 요청을 보내도 서버가 마비될 수 있음 → 일부 오픈 API는 계정 당 사용량이 제한되어 있음 (공식 문서에서 일일 및 월간 사용량 제한을 반드시 확인, 사용량 초과 시 요금이 청구될 수도 있음)
    - JSON : JavaScript Object Notation의 약자. 경량의 텍스트 기반의 데이터 형식 (통신 방법이나 프로그래밍 문법이 아님)
    
    ```python
    import json #별도의 설치없이 사용 가능, 내장 라이브러리임
    
    # json 데이터
    json_data = '''
    {
        "name": "김싸피",
        "age": 28,
        "hobbies": [
                "공부하기",
                "복습하기"
                ]
    }
    '''
    
    # print(json_data['name']) # string 형식이기 때문에 불가능
    
    data = json.loads(json_data) # json 타입 문자열이 dict 형식 자료로 바꿈
    print(data['name']) # 원하는 데이터 key를 입력해서 꺼낼 수 있음
    ```
    
    - 파싱(Parsing): 데이터를 의미 있는 구조로 분석하고 해석하는 과정 + 원하는 형태로 변환
    
    ### OPEN API 실습
    
    ```python
    import requests
    
    #OpenWeatherAPI KEY : 9d65bf88bb4d28d79c14c57b5c6eecc6
    API_key = '9d65bf88bb4d28d79c14c57b5c6eecc6'
    lat = 37.56
    lon = 126.97
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
    
    data = requests.get(url).json()
    print('도시: ', data['name'])
    print('현재 온도: ', data['main']['temp'] - 273.15)
    """
    도시:  Seoul
    현재 온도:  30.340000000000032
    """
    
    city = 'Busan'
    country_code = 'kr'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_key}'
    data = requests.get(url).json()
    print('도시: ', data['name'])
    print('날씨 설명: ', data['weather'][0]['description'])
    """
    도시:  Busan
    날씨 설명:  broken clouds
    """
    ```



# 7/28 관통 PJT2
## 데이터 사이언스

- 다양한 데이터로부터 새로운 지식과 정보를 추출하기 위해 과학적 방법론, 프로세스, 알고리즘, 시스템을 동원하는 융합 분야
- 컴퓨터 과학, 통계학, 수학 등 다양한 학문의 원리와 기술을 활용

### 필요한 정보를 추출하는 5가지 단계

1. 문제 정의 : 해결하고자 하는 문제 정의 → ex) 구글 주식이 오를까?
2. 데이터 수집 : 문제 해결에 필요한 데이터 수집 → ex) 과거 구글 주가, 기사, 정책 등 어떤 데이터를 중점적으로 분석할 것인지 정하고 수집
3. 데이터 전처리(정제) : 실질적인 분석을 수행하기 위해 데이터를 가공하는 단계
4. 데이터 분석 : 전처리가 완료된 데이터에서 필요한 정보를 추출하는 단계
5. 결과 해석 및 공유 : 의사 결정에 활용하기 위해 결과를 해석하고 시각화 후 공유하는 단계

### 데이터 수집

- 웹 스크레핑(Web Scraping): 웹 페이지에서 데이터를 추출하는 기술
- 웹 크롤링(Web crawling): 웹 페이지를 자동으로 탐색하고 데이터를 수집하는 기술
- Open API 활용: 공개된 API를 통해 데이터를 수집
- 데이터 공유 플랫폼 활용: 다양한 사용자가 데이터를 공유하고 활용할 수 있는 온라인 플랫폼
    - 종류: 캐글, Data.world, 데이콘, 공공데이터포털 등

- 데이터 수집 - 캐글(Kaggle)
    - 데이터 분석 경진대회 플랫폼
    - 기업 및 단체에서 데이터와 해결 과제를 등록하면, 데이터 과학자들이 이를 해결하는 방법을 개발하고 경쟁할 수 있는 플랫폼
    - 경진 대회, 데이터셋 공유, 토론 등의 기능이 가능

### CSV

- 몇 가지 필드를 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일
- 일반적으로 표 형식의 데이터를 CSV 형태로 많이 사용
- 저장, 전송 및 처리 속도가 빠르며, 처리 가능한 프로그램이 다양합니다.
- 또는 json, html 등의 파일 형식이 있음

### 데이터 전처리(정제)

- 데이터 전처리 단계는 분석을 진행하지 전 데이터를 정제하는 단계
- 불완전하거나 오류가 있는 데이터를 제거하며 데이터의 품질을 개선
- 중복 데이터 제거
- 분석하기 적절한 형식으로 데이터를 변환

## 주요 파이썬 패키지

### Numpy

- 수학 계산용 패키지
- 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 파이썬 패키지
- 장점:
    - Numpy 행렬 연산은 데이터가 많을수록 Python 반복문에 비해 훨씬 빠르다. → 내부적으로 C로 구성되어져 있음
    - 다차원 행렬 자료 구조를 제공하여 개발하기 편하다.
- 특징:
    - CPython(공식 사이트의 Python) 에서만 사용 가능
    - 행렬 인덱싱(Array Indexin) 기능 제공
    

### Pandas

- Numpy의 한계
    - 유연성(데이터를 레이블에 붙이거나, 누락된 데이터로 작업)이 부족함
    - 그룹화, 피벗 등 구조화가 부족함
- Pandas는 마치 프로그래밍 버전의 엑셀을 다루듯 고성능의 데이터 구조를 만들 수 있음
- Numpy 기반으로 만들어진 패키지로, Series(1차원 배열)과 DataFrame(2차원 배열)이라는 효율적인 자료구조 제공

### Matplotlib

- Python에서 데이터 시각화를 위해 가장 널리 사용되는 라이브러리
- 다양한 종류의 그래프와 도표를 생성하고 데이터를 시각적으로 표현할 수 있습니다.


# 10/6 관통 PJT4
# 금융 프로젝트

## Django에서 Data Science 활용하기

→ Matplotlib, Pandas, Numpy를 Django에서 구동함

- 알아야 할 내용
    - 데이터 사이언스 3종 패키지 사용 방법
    - Django 기본 사용 방법
        - 웹페이지 구성(template)
        - 데이터 전달(view → template)
- 파이썬  BytesIO 패키지

## view에서 template으로 이미지 전달하기

- view에서 template으로 이미지 형식의 데이터를 직접 전달할 수 없다
- 저장된 이미지의 경로를 전달하여 template에서 출력해야 함
- matplotlib의 그래프를 버퍼에 이미지 형식으로 저장 후 저장된 경로를 전달
    - buffer(버퍼) : 임시로 데이터를 저장하는 공간
- python “BytesIO” 클래스
- 파이썬의 내장 모듈인 “io” 모듈에 포함된 클래스
- 메모리 내에 데이터를 저장 및 조작할 수 있는 기능 제공

```python
import base64
from io import BytesIO

def test(request):
    # plot 작성
    plt.switch_backend('Agg') # 화면에 플롯팅되는 것을 막고, 차트를 이미지로 넘기는 설정 (안하면 main loop 어쩌구 에러가 발생)
    plt.clf() # plot 초기화 -> 현재 figure 지우기
    plt.figure(figsize=(10, 7)) # -> figure size 설정

    # 그래프 이미지를 임시로 저장할 버퍼 생성
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    context = {
        # 저장된 이미지의 경로를 전달
        'chart_image': f'data: image/png;base64, {image_base64}',
    }
    
    return render(request, 'test.html', context)
```

[matplotlib backend](https://kongdols-room.tistory.com/78)



# 10/13 관통 PJT5
# 웹 크롤링 실습

- 구글에 검색해보고 어떤 깐풍기, 탕수육 중 무엇이 더 많이 검색되는지 알아보자..!
- 웹 페이지의 결과를 코드에서 어떻게 활용할 수 있을까?

## 데이터 수집

1. 누군가 업로드해 둔 데이터를 다운로드 받기 (ex: 캐글)
2. 누군가 만들어 둔 API server 를 활용하여 정보를 받아오기
3. 사람이 검색하는 것처럼 파이썬이 자동으로 검색 후 결과를 수집하는 방법 → 웹 크롤링
4. 웹 페이지(한 페이지)에서 데이터를 추출 → 웹 스크래핑

## 웹 크롤링

- 여러 웹 페이지를 돌아다니며 원하는 정보를 모으는 기술
- 원하는 정보를 추출하는 스크래핑과 여러 웹 페이지를 자동으로 탐색하는 크롤링의 개념을 합쳐 웹 크롤링이라고 부름

→ 웹 사이트들을 돌아다니며 **필요한 데이터를 추출하여 활용할 수 있도록 자동화된 프로세스**
## 프로세스

- 웹 페이지 다운로드 : 해당 웹 페이지의 HTML, CSS, JavaScript 등의 코드를 가져오는 단계
- 페이지 파싱 : 다운로드 받은 코드를 분석하고 필요한 데이터를 추출하는 단계
- 링크 추출 및 다른 페이지 탐색 : 다른 링크를 추출하고, 다음 단계로 이동하여 원하는 데이터를 추출하는 단계
- 데이터 추출 및 저장 : 분석 및 시각화에 사용하기 위해 데이터를 처리하고 저장하는 단계

### 준비 단계

- 라이브러리 설치:
    - requests : HTTP 요청을 보내고 응답을 받을 수 있는 모듈
    - BeautifulSoup : HTML 문서에서 원하는 데이터를 추출하는 데 사용
    - Selenium : 웹 애플리케이션을 테스트하고 자동화하기 위한 파이썬 라이브러리 / 웹 페이지의 동적인 컨텐츠를 가져오기 위해 사용함 (검색 결과 등)
    
    → $pip install requests beautifulsoup4 selenium

### 코드

- JavaScript 코드가 적용되어 있지 않은 사이트 크롤링

```javaScript
import requests
from bs4 import BeautifulSoup

def crawling_basic():
    // 가져올 웹 페이지 url
    url = 'https://quotes.toscrape.com/tag/love/'

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    // 예쁘게 출력하기
    # text = soup.prettify()

    // 1. 태그로 검색하기
    // 1.1 가장 첫 번째 태그에 해당하는 요소
    //크롤링할 때는 항상 페이지 분석 -> 검색
    title = soup.find('h1') # 첫 번째 h1 태그 가져오기
    print(f'제목: {title.text}')
    // 1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a')
    print(f'a 태그들: {a_tags}') # list 형태로 반환

    for a_tag in a_tags:
        print(f'a 태그 하나씩 : {a_tag.text}')


    // 2. CSS 선택자로 검색하기
    // 2.1 첫 번째로 CSS와 일치하는 요소
    quote = soup.select_one('.text')
    print(f'첫 번째 글: {quote.text}')
    // 2.2 일치하는 모든 요소
    quotes = soup.select('.text')
    print(f'첫 번째 글: {quotes}') # list 형태로 반환
    for quote in quotes:
        print(f'글귀 : {quote.text}')

    // 파일로 저장
    # with open('html.txt', 'w', encoding='utf-8') as file:
    //     file.write(text)

crawling_basic()
```



- JavaScript가 적용되어 있는 사이트 크롤링
```javaScript 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver # 자바스크립트가 모두 동작한 후의 HTML을 가져올 수 있는 라이브러리


def get_google_data(keyword):
    // 검색할 키워드는 search?q= 뒤에 옴
    url = f'http://google.com/search?q={keyword}'
    
    // response = requests.get(url)
    // html = response.text

    // soup = BeautifulSoup(html, "html.parser")
    // print(soup.prettify())

    // 크롬 브라우저가 열리고, 이 때 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    // 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    with open(f'crawling{keyword}_with_JS.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    
    // 필요한거 가져오기
    // ex) 검색결과 개수가 필요하다? -> 사이트에서 검색결과 요소의 태그, css, id 등이 뭔지 확인하고 유니크한거 확인해서 가져오기

    N_search = soup.select_one('#result-stats')
    print(f'검색결과 갯수: {N_search.text}')

    // 여러 개를 가져와보자 -> 공통적인 클래스, id 등을 찾아야 ㄴ함
    search = soup.select('.srKDX')
    for s in search:
        print(s)
        
get_google_data('탕수육')
```

[robots.txt](https://seo.tbwakorea.com/blog/robots-txt-complete-guide/)