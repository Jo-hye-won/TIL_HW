import sys
sys.stdin = open('input.txt')

def bfs(sit, sitj, N):
    visited = [[0] * N for _ in range(N)]
    que = []
    que.append((sti, stj))
    visited[sti][stj] = 1
    while que:   # 큐가 비어있지 않으면(큐가 비워질 때까지)
        i, j = que.pop(0)       # 0없이 하면 dfs가 된다 (디큐)
        if maze[i][j] == 3:     # 도착 성공했을때,
            return visited[i][j] - 2  # 지나온 칸 수 리턴(시작, 도착은 빼주기)
        # 인접하고 인큐된 적이 없으면
        # 인큐, 인큐표시
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            # 벽이 아니고, 방문하지 않은 경우
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                que.append((ni, nj))  # 인큐  ex.(1,2)를 넣음
                visited[ni][nj] = visited[i][j] + 1   # ni, nj는 i, j에서 한칸더 간곳이
                                                      # 거기까지 가는데 몇칸 걸렸는지 체크하려고
    return 0    # 3인 칸에 도달할 수 없는 경우

# 출발점 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)   # 거리
    print(f'#{tc} {ans}')