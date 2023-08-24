import sys
sys.stdin = open('input.txt')

    # 하 좌 우
dx = [1, 0, 0]
dy = [0, -1, 0]

def check(x, y):
    visited = [[0]*N for _ in range(N)]
    origin_y = y
    visited[x][y] = 1
    cnt = 0
    while x != 99:
        for k in range(3):
            di = x + dx[k]
            dj = x + dy[k]
            if 0 <= di < N and 0 <= dj < N and ladder[di][dj] and visited[di][dj] == 0:
                x, y = di, dj
                visited[di][dj] = 1
                cnt += 1
                break
    return [cnt, origin_y]


T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split()) for _ in range(100))]
    distance = 987654321
    y_gap = 0
    for i in range(N):
        if ladder[0][i] == 1:
            dis, ys = check(0, i)
            if distance > dis:
                distance = dis
                y_gap = ys
    print(f'#{tc} {y_gap}')
