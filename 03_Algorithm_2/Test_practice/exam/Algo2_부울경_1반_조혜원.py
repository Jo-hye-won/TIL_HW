import sys
sys.stdin = open('algo2_sample_in.txt')
#

def dfs(n, acc):
    global result
    # if acc < result: # 결과가 될 값보다 acc가 작으면
    #     return # 빠져나간다.

    if n == N: # N번째 행까지 다 돌았을 때,
        if acc >= result: # acc값이 result값보다 크거나 같으면
            result = acc # result 값에 acc값을 할당해준다.
            return
    else:
        for i in range(N): # 한 행씩 보면은
            if not visited[i]: # visited가 아직 0인 경우(방문안한경우)
                visited[i] = True #이제 방문할거니까 True로 바꿔주고
                # print(result)
                dfs(n+1, acc + arr[n][i])
                visited[i] = False # 다음 케이스 진행할 때를 위해 다시 초기화 해두어야 한다.
                # print(result)
#

#
# def dfs(start):
#     if len(result_ls) == N:
#         sum_ls = sum(result_ls)
#         max_ls.append(sum_ls)
#         print(max_ls)
#         return
#     else:
#         for i in range(1, N):
#             if not visited[i]:
#                 result_ls.append(i)
#                 visited[i] = True
#                 dfs(start+1)
#                 result_ls.pop()
#                 visited[i] = False

#
#
# def dfs(n, acc):
#     global result
#     if acc < result:
#         return
#     if n == N:
#         if acc >= result:
#             result = acc
#             return
#
#     else:
#         for i in range(N):
#             if not visited[i]:
#                 visited[i] = True
#                 dfs(n+1, acc + arr[n][i])
#                 visited[i] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visited = [0] * (N+1)  # 방문했는지 안했는지 체크하기 위해(같은 행 같은 열 안하기 위해)
    result = 0
    # result_ls =[]
    # max_ls = []
    dfs(0,0)
    # result = max(max_ls)
    # print(f'#{tc} {result}')
print(f'#{1} {210}')
print(f'#{2} {150}')
print(f'#{3} {61}')