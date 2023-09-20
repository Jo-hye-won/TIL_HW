import sys
sys.stdin = open('input.txt')

# 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수 작성하시오.

# S : 탐색 시작 노드
# 마지막으로 연락받은 대상의 번호를 출력,
    # 마지ㅏㅁㄱ으로 연락받은 사람이 여려 명이면, 가장 출석번호가 높은 학생을 반환
def BFS(S):
    q = [S]
    while q:
        S = q.pop()
        # 현재 조사 대상 S 노드가 진출차수가 없다면 빈리스트 변환 -> 순회 안함
        for i in G.get(S, []):
            if not visited[i]:
                visited[i] = 1
                q.append()
T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    from_to = list(map(int, input().split()))

    # 학생은 1번부터 100번까지 있다.
    # 0번은 없겠지만, 간선 정보에 각 학생 정보를 index로 쓰려면.. 이쪽이 편하다.
    visited = [0] * 101
    # 인접 행렬 or 인접 리스트
    G = {}
    # 전체 연락망 정보 개수 // 2 => 간선의 개수
    # 방향성 있는 그래프

    for i in range(N//2):
        # G.get(1, []) : G 키가 1인 값이 없으면 빈 리스트 변환
        # G.get(1, []) + [2] ->
        G[from_to[i*2]] = G.get(from_to[i*2], []) + [from_to[i*2 + 1]]

    last = BFS(S)
    # 마지막에 도착한 친구와 동일한 시간이 걸린
    # visited에 걸린시간 기록해둔 값이 같은 노드들만 출ㄹ력
    # 출석번호가 가장 높은 대상을 출력하고 종료
    for i in range(101, -1, -1):
        if visited[i] == visited[last]:
            print(f'#{tc} {i}')
            break
