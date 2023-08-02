import sys
sys.stdin = open('input.txt')

T = int(input())
# sums = 0
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    '''
    # print(arr)
[[45, 15, 10, 56, 23], [96, 98, 99, 40, 69], [96, 84, 49, 46, 34], [16, 64, 81, 4, 11], [10, 66, 85, 55, 14]]
[[44, 91, 64, 73, 62], [78, 72, 52, 73, 48], [44, 88, 55, 75, 24], [22, 72, 59, 26, 62], [87, 11, 64, 79, 40]]
[[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]]

    '''

    sums = 0 # 초기값 설정 순회하기 전에 해야함!!
    for i in range(N):      # 5행
        for j in range(N):  # 5열 순회하면서
            s = arr[i][j]   # 얘를 기준으로
                # sums = 0
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj  # 상하좌우
                if 0 <= ni < N and 0 <= nj < N:  # 이웃한 요소 없는거 주의
                    sums += abs(s - arr[ni][nj])    # 차의 절대값 초기화
    print(f'#{tc} {sums}')





                    # for k in range(4):  # 상하좌우로 비교하면서
                    #     B = s - arr[ni][nj]
                    #     if B <=

# for tc in range(1, T+1): # 테스트 케이스
#     for i in range(N):  # 5행
#         for j in range(N):  # 5열
#             s = arr[i][j]
#             for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 요롷게도 가능하다
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < N and 0 <= nj < N:
#
#
# arr = [list(map(int, input().split())) for _ in range(N)]  # input으로 리스트 만들기
#
# max_v = 0   # 모든 원소가 0 이상이라고 전제깔고 합니다.
# for i in range(N):  # 모든 원소 arr[i][j]에 대해..
#     for j in range(N):
#         # arr[i][j]중심으로
#         s = arr[i][j]
#         for di, dj in [[0, 1],[1,0],[0,-1],[-1,0]]:  # 요롷게도 가능하다
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < N:     # 배열을 벗어나지 않으면
#                 s += arr[ni][nj]
#         # 여기까지가 주변 원소를 포함한 합
#
#         if max_v < s:  # s > max_v 로 하지말고 헷갈리니까
#             max_v = s
# print(max_v)
#
#
# max_v = 0   # 모든 원소가 0 이상이라고 전제깔고 합니다.
# for i in range(N):  # 모든 원소 arr[i][j]에 대해..
#     for j in range(N):
#         # arr[i][j]중심으로
#         s = arr[i][j]
#         for p in range(1, m):
#             for di, dj in [[0, 1],[1,0],[0,-1],[-1,0]]:  # 요롷게도 가능하다
#                 ni, nj = i + di*p, j + dj*p
#                 if 0 <= ni < N and 0 <= nj < N:     # 배열을 벗어나지 않으면
#                     s += arr[ni][nj]
#         # 여기까지가 주변 원소를 포함한 합
#
#         if max_v < s:  # s > max_v 로 하지말고 헷갈리니까
#             max_v = s
# print(max_v)
