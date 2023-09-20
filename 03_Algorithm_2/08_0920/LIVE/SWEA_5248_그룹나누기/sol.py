import sys
sys.stdin = open('input.txt')

# 그룹 나누기 _ 몇 개의 조가 만들어지는가?

def dfs(v):
    global cnt
    # cnt += 1
    visited[v] = 1
    # cnt += 1
    for next in range(len(graph[v])):
        # cnt += 1
        to = graph[v][next]
        if visited[to]:
            continue
        dfs(to)

        # cnt += 1


T = int(input())
for tc in range(1, T+1):
    # N = 총 학생수
    # M = 투표지(간선 개수)
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    cnt = 0

    # 인접리스트 만들기
    graph = [[] for _ in range(N+1)]
    # print(graph)

    for i in range(M):
        v1 = numbers[i*2]
        v2 = numbers[i*2 + 1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    '''print(graph)
    [[], [2], [1], [4], [3], []]
    [[], [2], [1, 3], [2], [5], [4]]
    [[], [], [3], [2], [5, 6, 7], [4], [4], [4]]
    '''
    visited = [0] * (N + 1)

    for i in range(1, N+1):
        if visited[i] == 0: # 방문하지 않았다면
            cnt += 1
            dfs(i)
    print(f'#{tc} {cnt}')





    # print(f'#{tc} {result}')