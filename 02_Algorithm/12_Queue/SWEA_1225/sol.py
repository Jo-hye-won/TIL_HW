import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
for tc in range(1, T+1):
    TC = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    # 내 데이터의 맨 마지막 값이 0이면 종료
    # 0이 아닌동안 반복
    while data[-1] != 0:
        cnt += 1 # cnt값 1씩 증가하게 하기
        # 첫번째 값에서 cnt1씩 올라가면서 빼줌
        data.append(data.pop(0)-cnt)
        if cnt == 5:  # 5까지 감소가 한 사이클이라서
                    # 다음 사이클 돌기 위해 cnt 초기화시켜줌
            cnt = 0
        if data[-1] < 0:  # 음수일경우
            data[-1] = 0    # 0으로
    print(f'#{TC}', end=' ')
    for j in data:
        print(j, end=' ')
    print()




