import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ls = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                x, y = j, i

                while x < n and arr[i][x] != 0:
                    x += 1

                while y < n and arr[y][j] != 0:
                    y += 1

                if arr[i][j] != 0:
                    ls.append((y-i, x-j))

                for a in range(i, y):
                    for b in range(j, x):
                        arr[a][b] = 0

        ls.sort(key=lambda a: (a[0]*a[1], a[0]))

    print(f'#{tc}', len(ls), end=' ')
    for x,y in ls:
        print(x, y, end=' ')
    print()



