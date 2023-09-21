import sys
sys.stdin = open('input.txt')
import heapq
# 최소 이동 거리

def dijkstra():
    # 비교 대상이 될 가중치 정보
    dist = [E * 100] * (V + 1)
    # 우선순위 큐
    priority_queue = []
    # 출발점 초기화
    # heap (가중치, 노드번호)
    heapq.heappush(priority_queue, (0, 0))
    dist[0] = 0

    while priority_queue:
        W, node = heapq.heappop(priority_queue)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있는지 확인
        if dist[node] < W: continue

        for next in arr[node]:
            # 갈 수 있는지 판별
            # 내 간선정보의 현재 노드의 다음 인접 노드 번호 출력한 값이 E*100이 아니면
            if arr[node][next] != E*100:
                next_node = next
                cost = arr[node][next]

                next_cost = cost + W

                if dist[next_node] <= next_cost:
                    continue
                dist[next_node] = new_cost
                heapq.heappush(priority_queue, (new_cost, next_cost))
        return dist[V]

        # 인접노드



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[E*100] * (V+1) for _ in range(V+1)]

    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S][E] = W
    print(arr)
    print(f'#{tc} {dijkstra()}')