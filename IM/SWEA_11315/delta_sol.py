import sys
sys.stdin = open('input.txt')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(N)]

    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                for p in range(8):
                    nx, ny = i, j
                    cnt = 0
                    while 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[p]
                        ny += dy[p]
                    if cnt >= 5:
                        ans = 'YES'

    print(f'#{tc} {ans}')