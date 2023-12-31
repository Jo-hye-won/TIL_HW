import sys
sys.stdin = open('input.txt')
'''
제공할 수 있으면 'Possible'
아니라면 'Impossible'
'''

T = int(input())
for tc in range(1, T+1):
    # N손님수, M초마다 K개 생산  74 60 97
    N, M, K = map(int, input().split())
    # print(N, M, K)

    # N명이 각각 도착하는 시간
    visited_time = list(map(int, input().split()))
    visited_time.sort()  # 도착시간 순으로 정렬
    result = 'Possible'
    for i in range(N):
        # i+1 번째 손님이 방문한 시간이
        # i 번째 손님이 방문한 시간까지의 붕어빵 생산량보다 커버리면
        # 붕어빵이 없어서 제공할 수가 없으니까
        # 아래와 같이 조건문을 달아준다.
        # 붕어빵 틀은 한번에 뿅 나온다~
        if i+1 > visited_time[i] // M * K:
        # if i + 1 > visited_time[i] * K // M :
            result = 'Impossible'
            break
    print(f'#{tc} {result}')

