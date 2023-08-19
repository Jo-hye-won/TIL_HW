import sys
sys.stdin = open('input.txt')

T = int(input())
di = [0, 1, 1]
dj = [1, 1, 0]

for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # print(arr)
    max_die = 0
    for i in range(N):
        for j in range(N):
            default = arr[i][j]
            for k in range(3):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    default += arr[ni][nj]
        if max_die < default:
            max_die = default


    print(f'#{tc} {default}')