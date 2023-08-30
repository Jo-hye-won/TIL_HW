import sys
sys.stdin = open('input.txt')

from collections import deque

di = [0, 1]
dj = [1, 0]


def bfs(x, y, val):
    q = deque()
    q.append((x,y,val))

    while q:
        x, y, val = q.popleft()

        for k in range(2):
            ni, nj = x + di[k], y+dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > val+MAP[ni][nj]:
                visited[ni][nj] = val + MAP[ni][nj]
                q.append((ni, nj, val+MAP[ni][nj]))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    bfs(0,0,MAP[0][0])
    print(f'#{tc} {visited[N-1][N-1]}')