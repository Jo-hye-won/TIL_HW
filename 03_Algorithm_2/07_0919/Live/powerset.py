# {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본적인 예제
# 이미 사용한 숫자는 사용하지 않도록


arr = [i for i in range(1, 4)]
path = [0] * 3

def backtracking(cnt):
    # 기저 조건
    # 숫자 3개를 골랐을 때 종료
    if cnt == 3:
        print(*path)
        return

    for num in arr:
        # 가지치기 - 중복된 숫자 제거
        # 조건을 작성하는 것이 핵심!!
        if num in path:
            continue
        # 들어가기 전 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt + 1)
        # 돌아와서 할 로직 ★
        path[cnt] = 0  # 초기화

backtracking(0)

'''
# 기본 구조
def func():
    # 재귀를 끝내는 기저 조건

    # 가지치기
    # 반복문
        # 가지치기

        # 재귀 들어가기 전
        # 재귀 함수 호출
        # 돌아와서 초기화
'''