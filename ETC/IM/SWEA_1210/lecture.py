import sys
sys.stdin = open('input.txt')

dx = [1, 0, 0]
dy = [0, -1, 1]

def search(x,y):
    visited = [[0]*100 for _ in range(100)]
    original_y = y
    visited[x][y] = 1

    while x != 99:
        # 조사 순서 하, 좌 우
        for k in range(3):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] and visited[nx][ny] == 0:
                x, y = nx, ny
                visited[nx][ny] = 1


    if data[x][y] == 2:
        return original_y
    else:
        return '실패'


for _ in range(10):
    tc = int(input())
    data = []
    for i in range(100):
        arr = list(map(int, input().split()))
        data.append(arr)


    for i in range(100):
        if data[0][i] == 1:
            result = search(0, i)
        if result != '실패':
            break

    print(f'#{tc} {result}')