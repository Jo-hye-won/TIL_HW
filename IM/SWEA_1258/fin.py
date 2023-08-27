import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x, y = j, i
                while x < N and arr[i][x] != 0:
                    x += 1

                while y < N and arr[y][j] != 0:
                    y += 1

                result.append((y-i,x-j))

                for a in range(i, y):
                    for b in range(j, x):
                        arr[a][b] = 0

        result.sort(key=lambda a: (a[0]*a[1], a[0]))

    print(f'#{tc}', end=' ')
    print(len(result), end= ' ')
    for i in result:
        print(*i, end=' ')