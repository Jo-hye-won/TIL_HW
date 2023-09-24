import sys
sys.stdin = open('input.txt')


def permutation(n, acc):
    global result
    if acc > result:
        return
    if n == N:
        if acc < result:
            result = acc
        return

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                permutation(n+1, acc + arr[n][i])
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visited = [0] * N
    result = sum(sum(arr, []))
    print(result)
    permutation(0, 0)
    print(f'#{tc} {result}')

#
#
# # nPr : n == r
# # r : 사용중인 원소의 개수
# # acc : 현재 경우의 수까지 누적된 값
# def permutation(r, acc):
#     global result
#     if acc > result:
#         return
#     # 종료 시점
#     if r == N:
#         # 무슨 일 할건데?
#         # 모든 공장 순회 다했고,
#         # 각 공장의 비용을 다 더했는데
#         # 비교 대상보다 acc의 값이 작으면
#         if acc < result:
#             # 그 값이 최솟값
#             result = acc
#         return
#     else:
#         # 모든 공장이 하나씩은 만들어야하니
#         for i in range(N):
#             if not visited[i]:
#                 visited[i] = True
#                 # A 공장의 1번 제품 생산비용을 acc에 누적 해본다음
#                 permutation(r+1, acc+arr[r][i])
#                 # A 공장이 1번 제품을 안쓰고, 2번 제품을 썼을 때
#                 visited[i] = False
#
# T = int(input())
# for tc in range(1, T+1):
#     # 배열의 길이
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # arr[?][i] 사용 여부
#     visited = [0] * N
#     # 비교 대상군
#     result = sum(sum(arr, []))
#     permutation(0, 0)
#     print(f'#{tc} {result}')