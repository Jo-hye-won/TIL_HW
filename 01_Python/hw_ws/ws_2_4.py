information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

'''
- 작가와 작품 목록 참고
- 허균 : 홍길동전, 장생전, 도문대작
- 임제 : 수성지, 백호집, 원생몽유록
- 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
'''

# 딕셔너리에 key, value 값 추가하는 방법
information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

print(information) # 딕셔너리에 들어간 것 확인 가능!!

# 출력하기    
# 1. 이렇게 하나하나 키와 벨류를 불러와서 출력해도 되고
# print(f'{authors[0]} : {books[1]}')
# print(f'{authors[1]} : {books[3]}')
# print(f'{authors[2]} : {books[4]}')
# print(f'{authors[3]} : {books[0]}')
# print(f'{authors[4]} : {books[2]}')

# 2. .items()를 사용해서 키랑 벨류 출력해도 된다.
for key,value in information.items():
    print(f'{key} : {value}')
      