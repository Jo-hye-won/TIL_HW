'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# MST
def prim(start):
    # 방문 정보
    visited = [0] * (V+1)
    visited[start] = 1 # 시작정보
    # 가중치 누적값
    result = 0
    # heap 자료구조를 안쓴다 -> 모든 정점 조사
    for _ in range(1, V):
        # 다음 조사 대상
        next = 0
        # 가중치 비교 대상
        min_val = 1e9
        for i in range(V+1):
            # 이미 방문한 지점을 기준으로
            if visited[i] == 1:
                for j in range(V+1):
                    # 한번 방문한 적 있었던 i의 인접노드 j
                    # 인접행렬을 진출 가능한 노드에 대해서만 가중치를 기록
                    '''
                    [0, W, 0, W]
                    '''
                    # 진출 가능하고, 다음 노드 j를 방문하지 않았고
                    if arr[i][j] > 0 and not visited[j]  and min_val > arr[i][j]:
                        next = j
                        min_val = arr[i][j]
        result += min_val  # 가중치 누적
        visited[next] = 1
    return result


# 노드, 간선
V, E = map(int, input().split())
# 간선 정보
arr = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    # 진출, 진입, 가중치
    S, E, W = map(int, input().split())
    # 무방향 그래프이므로 양쪽 모두 진출/진입 노드 정보 입력
    arr[S][E] = W
    arr[E][S] = W
print(arr)
print(prim(0))