import sys
sys.stdin = open('input.txt')

# 시작점 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(starti, startj, N):
    visited = [[0] * N for _ in range(N)]
    que.append((starti, startj))
    visited[starti][startj] = 1
    while que:
        x, y = que.pop()
        if maze[x][y] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = x + di, y + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                que.append((ni, nj))
                visited[ni][nj] = 1
    return 0

T = 10
for tc in range(1, T+1):
    TC = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    que = []
    starti, startj = find_start(N)
    result = bfs(starti, startj, N)
    print(f'#{TC} {result}')