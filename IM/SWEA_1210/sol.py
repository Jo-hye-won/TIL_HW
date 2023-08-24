import sys
sys.stdin = open('input.txt')

    # 하, 좌, 우
dx = [1, 0, 0]
dy = [0, -1, 1]

def search(x,y):
    #들린 지점은 1로 표시해서 다시 돌아가지 않게 만들기 위함
    visited = [[0]*100 for _ in range(100)]
    original_y = y  # 출발지점의 x좌표
    visited[x][y] = 1

    while x != 99:  # 마지막 행까지 갈 동안
        for k in range(3):  # 하, 좌, 우 방향 조사하면서
            ni = x + dx[k]
            nj = y + dy[k]
            # ni,nj가 범위 안에 있고 갈 수 있는 길이며, 들린적이 없으면 가야지
            if 0 <= ni < N and 0 <= nj < N and ladder[ni][nj] and visited[ni][nj] == 0:
                x, y = ni, nj  # 그리고 거기를 기점으로 또 search 해야함
                visited[ni][nj] = 1   # 들렀음을 표시해주자

    if ladder[x][y] == 2: # 2가 적혀있는 도착점에 다다르면
        return original_y    # 출발위치의 x좌표인 y를 반환
    else:
        return "실패"


T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # print(ladder)
    for i in range(N):
        if ladder[0][i] == 1:
            result = search(0, i)
        if result != "실패":
            break

    print(f'#{tc} {result}')
