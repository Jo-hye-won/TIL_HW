import sys
sys.stdin = open('input.txt')

def dfs(i, j, arr):
    if arr[i][j] == '3':
        return 1
    else:
        arr[i][j] = '1'  # 지나간 곳은 1로
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1':
                if dfs(ni, nj, arr):
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                result = dfs(i,j,miro)

    print(f'#{tc} {result}')