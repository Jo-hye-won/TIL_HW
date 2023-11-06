import sys
sys.stdin = open('input.txt')

T = int(input())
N = 9

di = [0,0,1,1,1,2,2,2]
dj = [1,2,0,1,2,0,1,2]


for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 가로
    garo = arr

    # 세로
    sero = []
    for i in range(N):
        col = []
        for j in range(N):
            col.append(arr[j][i])
        sero.append(col)
    # print(sero)
    result = 1
    # 9칸 내에서
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            point = arr[i][j]
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    point += arr[ni][nj]

            for ga, se in zip(garo, sero):
                if sum(ga) == sum(se) == point == 45:
                    continue
                else:
                    result = 0
                    break

    print(f'#{tc} {result}')
