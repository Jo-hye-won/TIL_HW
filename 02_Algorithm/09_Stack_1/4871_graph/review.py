import sys
sys.stdin = open('input.txt')

T = int(input())

def DFS(node):
    stack = [node]
    visited = [0] * (V+1)
    while stack:
        start = stack.pop()
        # if start == to:
        #     return 1

        # 여기 있으면 for 안에 있을 때보다 반복해서 봐야 할 것이 많아지기 때문에
        # if start == to:  # start가 도착노드 to에 간 적이 있으면
        #   return 1  # 1 반환

        if visited[start] == 0:
            visited[start] = 1
            for next in range(V+1):
                # if matrix[start][next] == 1 and visited[next] == 0:
                if not visited[next] and matrix[start][next] == 1:
                    # visited[next] = 1
                    stack.append(next)

                # 여기서 간적이 있는지 확인하는게 더 효율적이다.
                if start == to:  # start가 도착노드 to에 간 적이 있으면
                    return 1  # 1 반환

    else:             # 도착노드 못가서 경로를 찾지 못한 경우
        return 0      # 0 반환

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        S, G = map(int, input().split())
        matrix[S][G] = 1
    Go, to = map(int, input().split())
    print(f'#{tc} {DFS(Go)}')

