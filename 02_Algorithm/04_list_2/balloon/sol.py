import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_ = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for k in range(4):
                ai = i + di[k]
                aj = j + dj[k]
                if 0 <= ai < N and 0 <= aj < M:
                    s += arr[ai][aj]
            if max_ < s:
                max_ = s
    print(f'#{tc} {max_}')