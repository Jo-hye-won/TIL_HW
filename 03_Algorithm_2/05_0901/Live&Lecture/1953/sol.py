import sys
sys.stdin = open('input.txt')

# [모의 SW역량테스트] 탈주범 검거

# 탐색 가능범위(내가 어디 있느냐에 따라 달라지는 탐색 가능한 범위)
tunnel = {
    1: [(-1,0), (1,0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}
# 좌표 x, y
# cnt : 이동한 시간
def BFS(x, y, cnt):
    global result
    q = [(x, y, cnt)]
    visited[x][y] = 1
    while q: # q 에 값이 있는 동안
        x, y, cnt = q.pop(0)
        # 아직 q에 조사 대상이 남아 있어도 끝낼 상황
        if cnt == L:  # 현재 조사하는데 걸린 시간이, 최대 시간이 되면 종료
            return
        # 다음 위치 조사 가능한지 조사를 시작했다?
        # 즉, 최종 결과값이 1 증가했다
        result += 1
        # 내 현재 좌표의 터널 정보를 알아내야 한다.
        # 그 터널의 다음 방문 가능 정보
        for dx, dy in tunnel[arr[x][y]]:
            nx = x + dx
            ny = y + dy
            # 조사범위 체크
            # 다음조사 위치가 0은 아니고
            # 아직 방문한 적 없고
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visited[nx][ny]:
                for cx, cy in tunnel[arr[nx][ny]]:
                    # dx, dy | x, y 에서 이동할 수 있는 방향 중 하나 (0, -1)
                    # cx, cy | nx, ny 에서 이동할 수 있는 방향 중 하나(0, -1)
                    if dx + cx == 0 and dy+cy == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
                        break

T = int(input())

for tc in range(1, T+1):
    # 가로, 세로, 시작좌표x, y, 시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [[0]*M for _ in range(N)]
    BFS(R, C, 0)
    print(f'#{tc} {result}')