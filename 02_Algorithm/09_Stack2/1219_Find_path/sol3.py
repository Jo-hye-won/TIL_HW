def dfs(vertext):
    visited[vertext] = True
    for i in stack[vertext]:
        if visited[i] == False:
            dfs(i)


for _ in range(10):
    t, Edges = map(int,input().split())
    arr = list(map(int,input().split()))

    # 정점이 방문되었는지?
    visited = [False] * 100
    # 갈수 있는 길
    stack = [[] for _ in range(100)]

    for i in range(Edges):
        stack[arr[i*2]].append(arr[i*2+1])

    dfs(0)

    result = int(visited[-1])

    print(f'#{t} {result}')