import sys
sys.stdin = open('input.txt')


# union 처리 -> 집합 x 와 집합 y를 하나의 집합으로 연합 이루게 하기
'''
1 2 2 3
[0 1 2 3]
[0 1 1 3] | x = 1, y = 2
[0 1 1 2] | x = 2, y = 3
-> x, y의 루트 노드가 누구인지 (집합의 대장이 누구인지 찾는 과정)
1 2 2 3
[0 1 2 3]
[0 1 1 3] | x = 1, y = 2
[0 1 1 2] 
|x = 2(2번 노드 집합의 대장을 찾아서 반환)
|[0 1 1 1] |x = 1, y = 3
'''
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    # parent[y] = x

    # 두 루트 노드의 rank가 동일하다면,
    # 어디에 누구를 붙이든 똑같으니 하나 정해서 증가시켜준다.
    if rank[x] == rank[y]:
        rank[x] += 1


# 내 조상이 누군지 찾아가는 함수
# 루트 => 자기 자신을 부모로 잡고 있는 노드가 될 때 까지 조사
def find_set(x):
    # x 노드의 부모가 자기 자신 : 즉, x가 루트노드다
    if parent[x] == x:
        return x # 루트 노드인 x를 반환
    else:
        find_set(parent[x])



# 상호배타집합 만들어서 하면 됨 ( 리스트 만들 필요 없음 )

T = int(input())
for tc in range(1, T+1):
    # N = 총 학생수
    # M = 투표지(간선 개수)
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 간선 정보를 모른다는 가정 하에
    # 최초의 각 노드들의 정보를 초기화
    # make_set : 각각의 집합 생성하기
    parent = list(range(N+1))
    # 각 노드가 자식 노드를 얼마나 연결하고 있는지를 초기화
    rank = [0] * (N+1)

    for i in range(M):
        x = numbers[i*2]
        y = numbers[i*2 +1]
        union(x, y)
    print(numbers)
    print(parent)
