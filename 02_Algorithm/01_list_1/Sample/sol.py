import sys
# open 함수의 인자는
# 내가 열고자 하는 파일의 경로와 이름.
sys.stdin = open('input.txt')

# input 함수의 반환은 항상 문자열
# 입력받은 값을 정수로 형변환 후 리스트에 담는다

data = list(map(int, input().split()))
print(data)