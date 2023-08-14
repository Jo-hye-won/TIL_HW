
def DFS(node):
    stack = [node]
    visited = [False] * (V + 1)
    while stack:    # stack에 (조사해야할 값)이 있는 동안
        start = stack.pop()
        if visited[start] == 0:
            visited[start] = True
        #     print(start, end=' ')
        for next in range(0, V + 1):
            if matrix[start][next] == 1:
                stack.append(next)
                print(start, end=' ')

# V = node의 개수
# E = Edge 간선의 개수
V, E = map(int, input().split())
data = list(map(int, input().split()))
matrix = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, E*2, 2):
    # print(i, i+1, data[i], data[i+1])
    matrix[data[i]][data[i+1]] = 1
    matrix[data[i+1]][data[i]] = 1

DFS(1)