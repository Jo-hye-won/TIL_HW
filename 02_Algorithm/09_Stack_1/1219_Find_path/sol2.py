def DFS(node):
    stack = [node]  # 스택에 받아오는 값(출발점) 넣고
    visited = [0] * 100  # 방문 표시할 리스트(0에서 99까지 표시해줘야 해서 100개 만듬)
    visited[node] = 1

    while stack:    # 스택에 값이 있는 동안
        now = stack.pop()
        if now == goal:
            return 1

        for next in range(100):
           if arr[now][next] == 1 and visited[next] == 0:
                stack.append(next)  # start를 스택에 넣어주자
                visited[next] = 1
    return 0


T = 10
start = 0   # 출발점
goal = 99   # 도착점

for tc in range(1, T+1):
    t, N = map(int, input().split())
    arr = [[0] * 100 for _ in range(100)]
    numbers_list = list(map(int, input().split()))

    for i in range(0, N * 2, 2):
        arr[numbers_list[i]][numbers_list[i+1]] = 1

    print(f'#{tc} {DFS(start)}')