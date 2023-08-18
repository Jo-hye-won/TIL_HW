'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력결과 : 1-2-3-4-5-7-6
'''

def bfs(s, V): # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)            # visited 생성
    que = []                         # 큐 생성
    que.append(s)                    # 시작점 인큐
    visited[s] = 1                   # 시작점 방문표시
    while que:                       # 큐에 정점이 있는 동안
        t = que.pop(0)                # 디큐
        print(t, end=' ')            # 방문한 정점에서 할 일
        for w in range(1, V+1):      # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if adj_l[t][w] == 1 and visited[w] == 0:
                que.append(w)
                visited[w] = visited[t] + 1
    print(visited)
V, E = map(int, input().split())     # 1번부터 V번 정점, E개의 간선
path = list(map(int, input().split()))
# 인접행렬 ---------------------------
adj_l = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = path[i*2], path[i*2 + 1]
    adj_l[v1][v2] = 1
    adj_l[v2][v1] = 1
# 여기까지 인접리스트 ---------------------------
bfs(1, V)
# bfs(2, V)