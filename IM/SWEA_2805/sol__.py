# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # N : 농장의 길이
#     N = int(input())
#     # arr : 농장 수확물 배열
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # 로직
#     # 누적 변수
#     total = 0
#     # 열 우선순회를 하면서
#     s = e = N // 2  # 중간값으로 시작점과 끝점을 초기화 해준다...
#     for i in range(N):
#         # j 의 좌표값의 시작점과 끝점을 -1 + 1 하면서 진행...
#         for j in range(s, e + 1):
#             total += arr[i][j]
#         if i <= N // 2:
#             s -= 1
#             e += 1
#         else:
#             s += 1
#             e -= 1
#
#     # 출력
#     print(f"#{tc} {total}")
#
# """
# 1
# 5
# 14054
# 44250
# 02032
# 51204
# 52212
# """
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # N : 농장의 길이
#     N = int(input())
#     # arr : 농장 수확물 배열
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # 로직
#     # 누적 변수
#     total = 0
#     M = N // 2 # 중간값
#     k = 0
#     for i in range(N):
#         for j in range(M - k, M + k + 1):
#             total += arr[i][j]
#         if i <= N // 2:
#             k += 1
#         else:
#             k -= 1
#
#     # 출력
#     print(f"#{tc} {total}")


"""
1
5
14054
44250
02032
51204
52212
"""

T = int(input())
for tc in range(1, T + 1):
    # 입력
    # N : 농장의 길이
    N = int(input())
    # arr : 농장 수확물 배열
    arr = [list(map(int, input())) for _ in range(N)]

    # 누적합 변수
    total = 0
    # 중간값
    M = N // 2
    # 중간 좌표인 (M, M)을 기준으로 해서, (i, j)와의 좌표거리가 M이하인 좌표라면
    # 수확을 해도 되는 범위...(좌표이다...)
    for i in range(N):
        for j in range(N):
            if abs(M - i) + abs(M - j) <= M:
                total += arr[i][j]

    # 출력
    print(f"#{tc} {total}")