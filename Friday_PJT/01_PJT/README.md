# 01_pjt
1. 금융감독원에서 API KEY를 받는다
2. 메일로 온 API KEY 주소를 복사해서 가져온다. -

## 문제 1_데이터 추출 - Key값 출력하기
- 전체 정기예금의 응답을 json형태로 변환 후 아래와 같이 Key값만 출력하도록 구성합니다.

3. [오픈 API상세 및 테스트_정기예금 json 요청변수](https://finlife.fss.or.kr/finlife/api/fdrmDpstApi/list.do?menuNo=700052) url에 할당

4. import requests, import pprint  젤 위에서 불러와두기 

> 이미 문제 젤 위에 있었음 내가 넣을 필요 없었다.

```bash import requests import pprint 

api_key = "b2ebdfc07634460b8a3e7b9b255e1836"  # 내가 메일로 전달받은 API KEY

> 다시받은 api_key : 44cc0b14b613e1c87fb6ba503b33b1ef

def get_deposit_products():  # get_deposit_priducts 함수를 정의해보자.

# 전체 정기예금의 응답 url
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={aip_key}&topFinGrpNo=020000&pageNo=1'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url)
    print(response.json())
    # result = requests.get(url).json()  # API 요청 보내기
    # print(result)
```
> 이렇게 했는데 왜 아무것도 안나올까? : api_key를 잘못 받았었다.☆★☆★

```bash
def get_deposit_products():  # get_deposit_priducts 함수를 정의해보자.
    api_key = "44cc0b14b613e1c87fb6ba503b33b1ef"  # 내가 메일로 전달받은 API KEY
    # 전체 정기예금의 응답 url
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
   
     # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    
    result = requests.get(url).json()  # API 요청 해서 JSON -> dict 데이터 변환
    return result["result"].keys()
```
> 이렇게 해서 해결!!!

5. result["result"].keys()를 사용해서 key값만 불러오기

6. 뭔가를 잘못만져서 requests를 읽을 수 없다고 할 때는 위에 run all 누르자!!!! ★


## 문제 2_데이터 추출 - 전체 정기예금 상품 리스트
- 1번 문제를 풀고나서 바로 쉽게 풀렸다.


## 문제 3_데이터 가공_전체 정기예금 옵션 리스트
```bash
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "44cc0b14b613e1c87fb6ba503b33b1ef"

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    result = response["result"]
    return result
```

> ☆★☆★여기서 return을 해버리면 함수가 멈춰버리기 때문에 return을 하면 안된다. 밑에서 출력에 있는 return이랑 다른거다. ☆★☆★


```bash
    key_parsed = result["optionList"]   # optionList 값들을 넣어주고

    new_list = []    # 빈 리스트를 만들어 준다음에

    for i in range(len(key_parsed)):
        new_dict = {}      # 빈 딕셔너리를 만들어 주고
        new_dict['금융상품코드'] = key_parsed[i]['fin_prdt_cd'] 
        new_dict['저축 금리'] = key_parsed[i]['intr_rate']
        new_dict['저축 기간'] = key_parsed[i]['save_trm']
        new_dict['저축금리유형'] = key_parsed[i]['intr_rate_type']
        new_dict['저축금리유형명'] = key_parsed[i]['intr_rate_type_nm']
        new_dict['최고 우대금리'] = key_parsed[i]['intr_rate2']
        #  딕셔너리에 값들을 넣어주고

        new_list.append(new_dict)  # 딕셔너리를 리스트에 추가해준다. 
    return new_list
```


## 문제 4_데이터 가공_새로운 값을 만들어 반환하기
















 <!-- # 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'

# API 요청
response = requests.get(API_URL)

# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# 변환 데이터 출력
print(parsed_data)

# 변환 데이터의 타입
print(type(parsed_data))

# 특정 데이터 출력
print(parsed_data['name'])
print(parsed_data['username'])
print(parsed_data['company']['name']) --> -->