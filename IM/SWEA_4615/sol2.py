import sys
sys.stdin = open('input.txt')
'''
돌의 색이 1이면, 흑돌
돌의 색이 2이면, 백돌

'''
def f(i, j, bw, N):
    MAP[i][j] = bw # 주어진 돌 놓기

    for di, dj in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]:
        ni, nj = i + di, j + dj
        tmp= []
        while 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] == op[bw]:
            tmp.append((ni, nj))
            ni, nj = ni+di, nj+dj
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] == bw: # 보드 내부 같은색
            for p, q in tmp:
                MAP[p][q] = bw


B = 1
W = 2
op = [0, 2, 1]
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 변의 길이 M 돌 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]
    MAP = [[0]*N for _ in range(N)]
    # 중심부 4개의 돌 배치
    MAP[N//2-1][N//2-1] = W
    MAP[N // 2 - 1][N // 2] = B
    MAP[N // 2][N // 2 - 1] = B
    MAP[N // 2][N // 2] = W
    # print(MAP)

    for x, y, bw in play:
        f(x-1, y-1, bw, N)

    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == B:
                bcnt += 1
            elif MAP[i][j] == W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')