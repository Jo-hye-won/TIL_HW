import sys
sys.stdin = open('input.txt')

''' 
주어진 출발 노드에서 최소 몇 개의 간선을 지나면
도착 노드에 갈 수 있나?
'''
def bfs(s, v):
    visited = [0] * (V+1)
    que = []
    que.append((s, 0)) # 출발하는 노드 번호와, 몇번 이동해서 온건지
    visited[s] = 1
    # cnt = 0
    # low_length = 0
    while que:
        tmp = que.pop(0)
        t = tmp[0]
        cnt = tmp[1]
        # t, cnt = que.pop(0) 해도 됨

        # for w in matrix[t]:
        # if visited[t] == 0:
        #     visited[t] = 1
            # cnt += 1
        for next in range(1, V+1):
            if visited[next] == 0 and matrix[t][next] == 1:
                que.append((next, cnt+1))
                visited[next] = 1
                if next == G:
                    return cnt+1
                # cnt += 1
    return 0


T = int(input())

for tc in range(1, T+1):
    # V = 노드 개수, E = 간선 개수(방향성 없음)
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for t in range(E):  # E개의 줄에 걸쳐서
        # 간선 양쪽 노드 정보 v1, v2 주어짐
        v1, v2 = map(int, input().split())
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1
    S, G = map(int, input().split())
    # G = 0
    # print(matrix)

    print(f'#{tc}', bfs(S,G))

