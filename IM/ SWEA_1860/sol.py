import sys
sys.stdin = open('input.txt')
'''
제공할 수 있으면 'Possible'
아니라면 'Impossible'
'''

T = int(input())
for tc in range(1, T+1):
    # N손님수, M초마다 K개 생산
    N, M, K = map(int, input().split())
    # print(N, M, K)

    # N명이 각각 도착하는 시간
    visited_time = list(map(int, input().split()))
    visited_time.sort()  # 도착시간 순으로 정렬
    result = 'Possible'
    for i in range(N):
        if i+1 > visited_time[i]//M*K:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')

