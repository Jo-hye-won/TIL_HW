import sys
sys.stdin = open('input.txt')


def dfs(n, acc):
    global result
    if acc > result:
        return
    if n == N:
        if acc <= result:
            result = acc
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = True
                dfs(n+1, acc + products[n][i])
                visited[i] = 0



T = int(input())
for tc in range(T):
    N = int(input())
    products = [list(map(int, input().split())) for _ in range(N)]
    result = sum(sum(products,[]))
    # print(products) [[73, 21, 21], [11, 59, 40], [24, 31, 83]]
    visited = [0] * (N+1)
    dfs(0,0)
    print(f'#{tc} {result}')