import sys
sys.stdin = open('input.txt')

    # 하 좌 우
di = [1, 0, 0]
dj = [0, -1, 1]

def search(x, y):
    visited = [[0]*N for _ in range(N)]
    ori_x = y
    visited[x][y] = 1
    cnt = 0
    while x != 99:
        for k in range(3):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N and ladder[ni][nj] and visited[ni][nj] == 0:
                x, y = ni, nj
                visited[ni][nj] = 1
                cnt += 1
    return [cnt, ori_x]


T = 10
N = 100

for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]
    cnt_ls = []
    for i in range(N):
        if ladder[0][i] == 1:
            cnt_ls.append(search(0, i))

    cnt_ls.sort()
    print(f'#{tc} {cnt_ls[0][1]}')