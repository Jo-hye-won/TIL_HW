import requests
from pprint import pprint
import json


ttbkey = 'ttbhws97011631001'
query_type = 'Author'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101
aladdin = '파울로 코엘료'

URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={aladdin}&{query_type}=Title&{max_results}=10&{start}=1&SearchTarget={search_target}&output={output}&Version={version}"

def author_works():
    result = requests.get(URL).json()  # API 요청 해서 JSON -> dict 데이터 변환
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works())

    