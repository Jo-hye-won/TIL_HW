
def find(start, n, acc):
    if n == N:
        acc += path[start][0]
        lst.append(acc)
        return
    for i in range(1, N):
        if not visited[i]:
            visited[i] = True
            find(i, n+1, acc+path[start][i])
            visited[i] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    path = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    lst = []
    find(0,0,0)