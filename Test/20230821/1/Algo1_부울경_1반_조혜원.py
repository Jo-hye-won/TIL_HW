import sys
sys.stdin = open('algo1_sample_in.txt')

'''
풍선개수가 적은 경우 가능한 풍선만 터진다

'''
     # 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
T = int(input()) # 보너스 스테이지의 수
for tc in range(1, T+1):
    N = int(input()) # 격자의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    # min_sum = 4000
    for i in range(N):    # 기본 점수 먼저구하기
        for j in range(N):
            point = arr[i][j]
            for k in range(4):
                for l in range(1, arr[i][j]+1):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        point += arr[ni][nj]
            # print(point)
            if max_sum <= point:
                max_sum = point
            # if min_sum >= point:
            #     min_sum
    # print(max_sum,1)
    # print(min_sum,0)


    # 보너스 스테이지
    # 1. 한개의 풍선을 터트려 점수를 얻는다. 다시 동일한 풍선이 배치된다.
    # 2. 다시 풍선을 터뜨려 점수를 얻는다.
    # 동일과정 한번 더 반복하면서 최대점수와 최소 점수를 구하자
    min_sum = 4000 # N개의 줄이 최대 20이고 점수가 최대 9니까 9가 400개면 3600이고
                    # 3600보다 클 수는 없을테니까 근데 여유롭게 4000으로
    for a in range(N):
        for b in range(N):
            point2 = arr[a][b]
            for c in range(4):
                for d in range(1, arr[a][b]+1):
                    nni = a + di[c]*d
                    nnj = b + dj[c]*d
                    if 0 <= nni < N and 0 <= nnj < N:
                        point2 += arr[nni][nnj]
                # print(point2)
            if min_sum >= point2:
                min_sum = point2
        # print(point2)
    bonus = max_sum - min_sum  # 보너스 점수는 최대점수 최소점수의 차이

    print(f'#{tc} {bonus}')