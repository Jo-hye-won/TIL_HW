import sys
sys.stdin = open('input.txt')

def bfs(i, j, N):
    global rm
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = [(i, j)]
    cnt = 0
    while q:
        i, j = q.pop(0)
        cnt += 1
        if v[i][j] != 0:
            return cnt + v[i][j]-1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0<=nj<N and rm[i][j]+1 == rm[ni][nj]:
                q.append((ni, nj))
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rm = [list(map(int, input().split())) for i in range(N)]
    v = [[0] * N for i in range(N)]

    maxV = 0
    minV = 100000000
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                v[i][j] = bfs(i,j,N)
                if (maxV < v[i][j]):
                    maxV = v[i][j]
                    minV = rm[i][j]
                elif maxV == v[i][j]:
                    if minV > rm[i][j]:
                        minV = rm[i][j]
    print(f'#{tc} {minV} {maxV}')