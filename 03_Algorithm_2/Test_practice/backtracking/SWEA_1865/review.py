import sys
sys.stdin = open('input.txt')

def dfs(n, acc):
    global result
    if acc < result:
        return
    if n == N:
        if acc > result:
            result = acc
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(n+1, acc *numbers[n][i]*0.01)
                visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    # print(numbers)
    visited = [0] * (N+1)
    result = 0
    dfs(0,1)
    result *= 100
    print(f'#{tc} {result:7f}')