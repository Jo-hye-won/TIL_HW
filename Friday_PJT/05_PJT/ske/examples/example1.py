from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")
    
    # 눈으로 보기 좋게 출력
    print(soup.prettify())

    # 1. 태그로 검색하기
    # 1.1 가장 첫번째 태그에 해당하는 요소
    title = soup.find('a')
    print(f'제목 : {title}')
    print(f'제목 : {title.text}')
    # 1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        print(f'제목2 : {a_tag}')
        print(f'제목2 : {a_tag.text}')

    word = soup.select_one('text')
    print(f'첫번째글 = {word.text}')

    words = soup.select('.text')
    for w in words:
        print(f'글 : w{w.text}')


    # 파일로 저장하여 확인하기
    with open('soup.txt', 'w', encoding="utf-8") as file:
        file.write(soup.prettify())


# 검색 키워드 설정
keyword = "파이썬"
get_google_data(keyword)

