
# 0~9
# 1. make set : 집합을 만들어 주는 과정
parent = [i for i in range(10)]


# 2. find-set :
def find_set(x):
    if parent[x] == x:
        return x

    # return find_set(parent[x])

    # 경로 압축(size, height(rank)가 적은 쪽을 합쳐주는게 효율적일 것이다)
    parent[x] = find_set(parent[x])
    return parent[x]


# 3. union
def union(x, y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        print("싸이클 발생")
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


union(0, 1)

union(2, 3)

union(1, 3)

# 이미 같은 집합에 속해있는 원소를 한 번 더 union
# 싸이클 발생
union(0, 2)


# 대표자 검색
print(find_set(2))
print(find_set(3))

# 같은 그룹인 지 판별
target_x = 0
target_y = 2

if find_set(target_x) == find_set(target_y):
    print(f'{target_x}와 {target_y}는 같은 집합에 속해 있습니다.')
else:
    print(f'{target_x}와 {target_y}는 다른 집합에 속해 있습니다.')