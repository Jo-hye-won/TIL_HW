import sys
sys.stdin = open('input.txt')

    # 하, 좌, 우
dx = [0, 0, 1]
dy = [1, -1, 0]


def check(x, y):
    visited = [[0] * 100 for _ in range(N)]
    original = y
    visited[x][y] = 1
    cnt = 0
    while x != 99:
        for k in range(3):
            ni = x + dx[k]
            nj = y + dy[k]
            if 0 <= ni < N and 0 <= nj < N and ladder[ni][nj] and visited[ni][nj] == 0:
                x, y = ni, nj
                visited[ni][nj] = 1
                cnt += 1
                break
    return [cnt, original]

T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]
    distance = 987654321  # 가장 짧은 이동거리를 구하기 위해 비교할 초기값 설정
    ans_y = 0   # 시작점인 x좌표 구하기 위해 비교할 초기값 설정

    for i in range(N):
        if ladder[0][i] == 1:  # 첫번째 행의 값이 1이면 시작지점
            dis, y_cordi = check(0, i)  # 이동거리와, 그때의 x 좌표를 반환한다
            # print(dis, y_cordi)
            if distance > dis:  # 가장 짧은 이동거리를 찾는다
                distance = dis  # 그 때의 거리와
                ans_y = y_cordi # 그 때의 시작점 x좌표를 구한다.
    print(f'#{tc} {ans_y}')






