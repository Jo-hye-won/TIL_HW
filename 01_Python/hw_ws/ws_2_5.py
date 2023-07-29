catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
    ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
    ['성공의 열쇠', '내면의 변화', '목표의 달성']
]

# 깊은 복사를 통해서 원본과 백업본이 각각 존재하도록 한다.
import copy
backup_catalog = copy.deepcopy(catalog)

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''
# 문자열 벨류로 넣기 
catalog [3][0] = '성공을 향한 한 걸음'
catalog [3][1] = '내 삶의 변화'
catalog [3][2] = '목표 달성의 비밀'

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자(is/ is not)로 catalog와 backup_catalog를 비교한 결과를 출력하시오. 
print(catalog is backup_catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

