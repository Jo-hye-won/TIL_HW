import sys
sys.stdin = open('input.txt')






T = int(input())

for _ in range(T):
    N = int(input())
    path = [list(map(int, input().split())) for _ in range(N)]
    # print(path)
    visited = [0] * (N+1)

import sys
sys.stdin = open('input.txt')

'''
각 관리구역을 돌고 다시 사무실로 돌아와야 한다 
'''
# k = 현재 조사 대상
# acc = 누적값(구하려는 값_)


def perm(k, acc):
    global result
    if acc >= result:
        return
    # 언제까지 조사해야 하는가?
    if k == N:
        # 누적값과 result 갱신
        acc += arr[order[N-1]][0]
        result = min(acc, result)

    else:  # 도착 안했다
           # 내 위치부터 마지막까지
        for i in range(k, N):
            order[k], order[i] = order[i], order[k]
            perm(k + 1, acc + arr[order[k - 1]][order[k]])
            order[k], order[i] = order[i], order[k]


T = int(input())
for tc in range(1, T+1):
    # 방문해야 하는 대상 수
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 순열 만들기 위한 리스트
    order = [i for i in range(N)]
    result = 9874565498798797
    perm(1, 0)
    print(f'#{tc} {result}')