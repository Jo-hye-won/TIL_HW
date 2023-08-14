T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    max_b = 0
    for i in range(N):
        for j in range(M):
            point = arr[i][j]
            for k in range(4):
                ai = i + di[k]
                aj = j + dj[k]
                if 0 <= ai < N and 0 <= aj < M:
                    point += arr[ai][aj]
            if max_b <= point:
                 max_b = point
    print(max_b)
