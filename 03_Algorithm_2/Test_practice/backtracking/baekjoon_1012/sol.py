import sys
sys.stdin = open('input.txt')

# 1012번: 유기농 배추

N = int(input())

for _ in range(N):
    M, N, K = map(int, input().split())
    # print(K)
    # arr = [[] for _ in range(M)]
    # print(arr)
    field = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    for f in field:
        print(f)
    # for _ in range(M):
    #     X, Y = map(int, input().split())
    #     arr[X].append(Y)
    #     arr[Y].append(X)
    # print(arr)
