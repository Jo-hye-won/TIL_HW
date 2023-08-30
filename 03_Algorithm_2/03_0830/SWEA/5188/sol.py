import sys
sys.stdin = open('input.txt')

# di = [0, 1]
# dj = [1, 0]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     res = [[float('inf')] * N for _ in range(N)] # 최소값으로 바꿔주기 위해
#     res[0][0] = MAP[0][0]                        # 스타트 값 지정
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(2):
#                 ni, nj = i + di[k], j + dj[k]
#                 if 0 <= ni < N and 0 <= nj < N:
#                     s = res[i][j] + MAP[ni][nj]    # 누적으로 값 더해주기
#                     if res[ni][nj] > s:                  # 최소값 찾아주기
#                         res[ni][nj] = s
#     print(f'#{tc} {res[N-1][N-1]}')
#
#
#     # start = matrix[0][0]     # 맨왼쪽 위에서
    # goal = matrix[N-1][N-1]  # 요까지 이동할 때
    # print(matrix)
    # print(goal,'goal')


        # 하 우
di = [1, 0]
dj = [0, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    path = [[float('inf')] * N for _ in range(N)]
    path[0][0] = matrix[0][0]
    #
    # # 움직인 거리도 짧으면서
    # move_distance = 0
    # # 합계가 최소가 되야한다.
    # min_sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(2):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    chlthgkq = path[i][j] + matrix[ni][nj]
                    if path[ni][nj] > chlthgkq:
                        path[ni][nj] = chlthgkq
    print(f'#{tc} {path[N-1][N-1]}')

#                 #    visited.append((ny, nx))
#                 # 아래와 오른쪽 방면 확인하면서
#                 # 가장 합이 작은곳으로 가면서
#                 # 움직인 거리 +1 해주기
