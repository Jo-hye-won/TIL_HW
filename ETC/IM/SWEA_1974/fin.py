import sys
sys.stdin = open('input.txt')

T = int(input())
N = 9

# 3*3 확인할 때 쓸 델타
di = [0,0,1,1,1,2,2,2]
dj = [1,2,0,1,2,0,1,2]

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]

    garo = arr # 가로는 그대로 받아와주고

    # 세로
    # sero = list(map(list, zip(*arr))) # 전치행렬하는 방법
    sero = []
    for i in range(N):
        col = []
        for j in range(N):
            col.append(arr[j][i])
        sero.append(col)

    result = 1 # 조건에 안맞는일 없으면 1 출력할거다
    # 3*3 9칸 안에서
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            point = arr[i][j] # 3*3 행렬의 0,0 위치를 point로 잡아주고
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                # if 0 <= ni < N and 0 <= nj < N:
                point += arr[ni][nj] # 나머지 8칸을 더해준다.

            # point하나 정해졌을 때마다 검사하기
            for ga, se in zip(garo, sero): # 가로와 세로 배열에서 원소 하나씩 가져와서
                # print(ga)
                # 1-9까지의 총합이 45라서
                if sum(ga) == sum(se) == point == 45: # 원소 내의 숫자들의 합이 45이고
                                                    # 다 더해져있는 point도 45이면
                    continue # 계속 진행시키기
                else:  # 합이 45가 안되면
                    result = 0  # result 값을 0으로 변환시켜주기

    print(f'#{tc} {result}')
