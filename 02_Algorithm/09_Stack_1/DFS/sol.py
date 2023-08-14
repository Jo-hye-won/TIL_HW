import sys
sys.stdin = open('input.txt')


# 노드 번호를 받아서 해당 노드부터 조사를 시작
def DFS(node):
    # stack을 활용해 보자
    stack = [node]
    # 조사 여부 체크용 리스트
    visited = [False] * (V + 1)  # 노드가 7개인데, 7번 인덱스까지 필요하니까 7+1 개의 값을 가진 리스트
    # stack.append(node)
    # 언제까지 조사
    while stack:  # stack에 (조사해야할 값)이 있는 동안
        start = stack.pop()  # stack은 항상 LIFO 마지막에 들어간 요소 빼내서 쓸거다.
        # 다음 조사를 시작하기 전,
        # 해당 위치가 이미 조사 한 적이 있다면 안 가도록 체크 할 수 있는 방법
        # 이전 번에 방문 한적 없다면
        if visited[start] == 0:
            visited[start] = True  # 방문 했다.
            # 현재 위치 기준으로 다음 위치 조사
            # 0부터 V+1번 노드까지 모두 조사
            print(start, end=' ')
            for next in range(V, 0, -1):
                # 다음 조사 가능 여부
                if visited[next] == 0 and matrix[start][next] == 1:
                    stack.append(next)
                    # print(start, end=' ')


# V = node의 개수
# E = Edge 간선의 개수
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))

# 이동 가능 정보 2차원 리스트
matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 모든 간선 순회
# for i in range(E):
#     print(data[i * 2], data[i * 2 + 1])
for i in range(0, E * 2, 2):
    # print(i, i+1, data[i], data[i+1])
    matrix[data[i]][data[i + 1]] = 1
    matrix[data[i + 1]][data[i]] = 1
    '''
    matrix[1][2] = 1
    matrix[2][1] = 1

    matrix[data[0]][data[1]] = 1
    matrix[data[1]][data[0]] = 1

    matrix[data[2]][data[3]] = 1
    matrix[data[3]][data[2]] = 1
    '''

# print(V,E)
# print(data)
# from pprint import pprint
# pprint(matrix)
DFS(1)