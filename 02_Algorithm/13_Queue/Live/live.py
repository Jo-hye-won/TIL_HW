# BFS(너비우선탐색)

def BFS(g, v):
    visited = [0]*(n+1)             # n은 정점의 개수
    queue = []                      # 큐 생성
    queue.append(v)                 # 시작점 먼저 인큐 하고(큐에 삽입해주고)
    while queue:                    # 큐가 빌때까지 반복한다(큐가 비어있지 않은 경우)
        t = queue.pop(0)            # 디큐해서 큐에 있는 애 하나 꺼내서 (큐의 첫번째 원소 반환)
        if not visited[t]:          # 아직까지 방문한적 없는 곳이면
            visited[t] = True       # 방문표시해주고
            visit(t)                # 이 노드에 대해 해 줄일 (번호를 출력해) - 예시
            for i in G[t]:          # t와 인접인 모든 정점에 대해서
                if not visited[i]:  # 아직까지 방문한 적이 없는 곳이면
                    queue.append(i) # 인큐하기로 해

'''
위의 코드는 중복해서 인큐되는 상황이 생길 수 있음
따라서 아래의 코드처럼 중복안되게 바꿔주기
'''

def BFS(G, v, n):  # 그래프 g, 탐색 시작점 v
    visited = [0]*(n+1)             # n은 정점의 개수
    queue = []                      # 큐 생성
    queue.append(v)                 # 시작점 먼저 인큐 하고(큐에 삽입해주고)
    visited[v] = 1
    while queue:                    # 큐가 빌때까지 반복한다(큐가 비어있지 않은 경우)
        t = queue.pop(0)            # 디큐해서 큐에 있는 애 하나 꺼내서 (큐의 첫번째 원소 반환)
        visit(t)
        for i in G[t]:
            if not visited[t]:          # 아직까지 방문한적 없는 곳이면
                queue.append(i)
                visited[i] = visited[t] + 1  # n으로 부터 1만큼 이동
