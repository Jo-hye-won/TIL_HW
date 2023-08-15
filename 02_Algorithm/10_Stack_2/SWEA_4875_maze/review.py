import sys
sys.stdin = open('input.txt')

def dfs(i, j, arr): #
    if arr[i][j] == '3':  # 도착하면
        return 1         # 도착성공했으니까 1 리턴
    arr[i][j] = '1'      # 방문한 곳은 1로 변경하면서 다시 못가게 해두고
    for k in range(4):   # 상우하좌 돌면서
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1':  # 범위 안에 있고 아직 들리지 않은 곳이면
            if dfs(ni, nj, arr):   # 거기서 또 탐색해서 갈 곳이 있으면
                return 1           # 도착성공해서 1 리턴
    return 0  # 도착 못했으면 0리턴

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':  # 시작점을 찾으면
                result = dfs(i, j, miro)  # 거기서 깊이우선탐색 시작
    print(f'#{tc} {result}')