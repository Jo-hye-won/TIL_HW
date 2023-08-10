import sys
sys.stdin = open('input.txt')

T = int(input())

def DFS(node):
    stack = [node]
    visited = [False]*(V+1)
    while stack:
        start = stack.pop()
        if start == Goal:
            return 1
        if visited[start] == 0:
            visited[start] = True
        for next in range(0, V+1):
            if not visited[next] and matrix[start][next] == 1:
                stack.append(next)
                # print(stack)

    else:
        return 0

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 노드개수, 간선개수
    matrix = [[0]*(V+1) for _ in range(V+1)]
    # print(matrix)
    for i in range(E):  # E개의 줄에 걸쳐서
        S, G = map(int, input().split())   # 출발, 도착 노드 간선정보 주어짐
        matrix[S][G] = 1  # 간선이 향해서 갈 수 있는 곳 표시
        # DFS(S)
        # matrix[G][S] = 1 은 안해줘도 됨(양방향이 아니고 단방향이라서)

    Start, Goal = map(int, input().split())
    result = DFS(Start)
    print(f'#{tc} {result}')