import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 10개
N = 100     # 행,열 100 X 100


for tc in range(1, T+1):       # 테스트 케이스 10번 돌면서
    a = int(input())    # 젤위에 있는거 하나 이상한 입력 없애주고
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열만들어주기
    max_idx = 0  # 최종 가장 큰 값 구하기 위한 초기설정

    # hang_sum = 0  # 여기서 선언하면 안돼!! 그럼 i도 다 순회하고 나서야 초기회됨
    for i in range(N):  # 행을 100번 돌면서 합을 구합시다
        hang_sum = 0    # 행의 합을 구하기 위한 초기값 설정
                        # 한 행을 조회할때마다 초기화 되기 위해서 여기 있어야 함
                        # 변수 선언시점이 굉장히 중요함!!!★★
        for j in range(N):
            plus = arr[i][j]   # i가 0일때 j 0-100 돌고 / i가 1일때 j 0-100돌고 쭉쭉쭉 i= 100,  j=100까지
            hang_sum += plus    # hang_sum에 누적해서 더해주기
            if hang_sum > max_idx:      # 최종가장 큰값이랑 비교해서 큰 값을 max_idx에 저장
                max_idx = hang_sum
