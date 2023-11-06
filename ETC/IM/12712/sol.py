import sys
sys.stdin = open('input.txt')


T = int(input())

# 대각선인 경우
dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]

# 상하좌우인 경우
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 최대 파리수 찾는 함수 정의하기
def find_flies(N,M,arr,x,y):
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            point = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + x[k]*l
                    nj = j + y[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        point += arr[ni][nj]
            if max_cnt <= point:
                max_cnt = point
    return max_cnt

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = find_flies(N,M,arr,di,dj)
    b = find_flies(N,M,arr,dx,dy)

    if a > b:
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} {b}')