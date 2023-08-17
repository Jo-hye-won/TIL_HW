import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
for tc in range(1, T+1):
    TC = int(input())
    data = list(map(int, input().split()))

    # 내 데이터의 맨 마지막 값이 0이면 종료
    while data[-1] > 0:
        data.append(data.pop(0))

    cnt = 1
    while data[-1] != 0:
        if cnt >= 6:
            cnt = 1
        tmp = data.pop(0) - cnt
        data.append(tmp)
        cnt += 1
    if data[-1] <= 0:
        data[-1] = 0
print(f'#{tc}', end = ' ')
print(*data)





