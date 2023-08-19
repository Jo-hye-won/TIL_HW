import sys
sys.stdin = open('input.txt')


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flower = 0
    for i in range(N):
        for j in range(M):
            point = arr[i][j]
            for k in range(4):
                for l in range(1, arr[i][j] +1):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0<= nj < M:
                    point += arr[ni][nj]
        if max_flower <= point:
            max_flower = point

    print(f'#{tc} {max_flower}')