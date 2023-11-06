import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # a, b, c, d, color = map(int, input().split())
    coloring = [[0]* 10 for _ in range(10)]
    for i in arr:
        for j in range(i[0], i[2]+1):
            for k in range(i[1], i[3]+1):
                if i[4] == 1:
                    coloring[j][k] += 1
                else:
                    coloring[j][k] += 2
    purple = 0
    for x in range(10):
        for y in range(10):
            if coloring[x][y] == 3:
                purple += 1
    print(f'#{tc} {purple}')