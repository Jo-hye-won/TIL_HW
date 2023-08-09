import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # M : 풍선 개수
    # N : 줄 개수
    N, M = map(int, input().split())
    ball = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N):

        for j in range(M):
            s = ball[i][j]
            for k in range(4):
                for l in range(1, ball[i][j] + 1):
                    ni, nj = i + di[k] * l, j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        s += ball[ni][nj]
            if res < s:
                res = s
    print(f'#{tc} {res}')