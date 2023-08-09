import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N = 행 개수 / M = 열 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 오른쪽, 아래, 왼쪽, 위
    # di = [0, 1, 0, -1]
    # dj = [1, 0, -1, 0]

    sum_idx = 0
    for i in range(N):
        for j in range(M):
            point = arr[i][j]        # 터뜨린 풍선의 꽃가루 수
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0] ]:   # i,j 인접에 대해
                ai, aj = i, j
                for l in range(arr[i][j]):   # 터뜨린 풍선의 꽃가루 수(arr[i][j])만큼 퍼져서 터지는거
                    ai, aj = ai + di, aj+dj
                    if 0 <= ai < N and 0 <= aj < M:
                        point += arr[ai][aj]
            if sum_idx < point:
                sum_idx = point

    print(f'#{tc} {sum_idx}')