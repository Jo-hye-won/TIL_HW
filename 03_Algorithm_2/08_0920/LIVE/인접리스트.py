# 인접리스트
# 내가 갈 수 있는 지점만 저장하자
# 주의사항
    # 각 노드마다 갈 수 있는 지점의 개수가 다름
    # range 쓸 때 index 조심
# 메모리가 인접 행렬에 비해 훨씬 효율적이다.

# arr = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [0, 1, 0, 1, 0]
# ] => 인접행렬

arr = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]
# 파이썬은 딕셔너리로도 구현할 수 있다.
# arr = {
#     '0' : [1, 3],
#     '1' : [0, 2, 3, 4],
#     '2' : [1],
#     '3' : [0, 1, 4],
#     '4' : [1, 3]
# }

# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue
        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)


        for to in range(len(arr[now])-1, -1, -1):
            # 연결이 안되어있는것은 애초에 저장하지 않았으므로
            # 체크할 필요 없음
            # if arr[now][next] == 0:
            #     continue

            next = arr[now][to]

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            # 다음 방문할 지점
            stack.append(next)

    # 출력을 위한 반환
    return visited

print("dfs_stack = ", end=' ')
print(*dfs_stack(0))


# DFS - 재귀
# MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠르다.

visited = [0] * 5
path = [] # 방문 순서 기록


def dfs(now):
    # 기저 조건
    visited[now] = 1 # 현재 방문 지점 표시
    # print(now, end= ' ')
    path.append(now)

    # 인접한 노드들을 방문
    for to in range(len(arr[now])):
        # if arr[now][next] == 0:
        #     continue
        next = arr[now][to]
        if visited[next]:
            continue
        dfs(next)


print('dfs 재귀 = ', end=' ')
dfs(0)
print(*path)