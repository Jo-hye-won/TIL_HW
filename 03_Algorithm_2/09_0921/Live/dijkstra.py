

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
# 최단 거리 문제 유형
# 1. 특정 지점 -> 도착 지점까지의 최단 거리 : 다익스트라
# 2. 가중치에 음수가 포함되어 있네 ? : 밸만포드
# 3. 여러 지점 -> 여러 지점까지의 최단 거리
#       - 여러 지점 모두 다익스트라 돌리기 -> 시간 복잡도 계산 잘해야함
#       - 플로이드-워샬

# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자!
import heapq

# 입력 :
n, m = map(int, input().split())

# 인접리스트
graph = [[] for i in range(n)]
# 도착점, 가중치 가지고 있ㅇ야 함
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t,w])


# 1. 누적 거리를 계속 저장
INF = int(1e9) #최대값으로 1억 - 대충 엄청 큰 수
distance = [INF] * n

def dijkstra(start):
# 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_code 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네 ?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dijkstra(0)
print(distance)