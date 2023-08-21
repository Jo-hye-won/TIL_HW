import sys
sys.stdin = open('input.txt')

# 전위순회
def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(left[node]) #왼쪽 자식
        preorder(right[node])
# LVR
def inorder(node):
    if node != 0:
        inorder(left[node])  # 왼쪽 자식
        print(node, end=' ')
        inorder(right[node])

# LRV
def postorder(node):
    if node != 0:
        postorder(left[node]) #왼쪽 자식
        postorder(right[node])
        print(node, end=' ')

V = int(input())  # 정점수 = 마지막 정점 번호
E = V - 1  # tree의 간선 수 = 정점 수  - 1
edge = list(map(int, input().split()))

# 왼쪽자식, 오른쪽자식, 부모정보
left = [0] * (V+1)
right = [0] * (V+1)
parent = [0] * (V+1)

#  [왼쪽, 오른쪽, 부모]
tree = [[0]*3 for _ in range(V+1)]
print(tree)

# 간선 정보 전수 조사
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]  # p = 부모 /  c = 자식
    if left[p] == 0:  # 아직 왼쪽 자식이 기록되지 않았다면
        left[p] = c
    else:
        right[p] = c
    parent[c] = p  # 자식 번째에 부모를 집어 넣어서

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p
print(tree)

root = 0
for i in range(1, V+1):
    if parent[i] == 0:
        root = i
        break

# print(root)
# print(edge)
# print(left)
# print(right)
# print(parent)

print('--전위순회--')
preorder(root)
print()

print('--중위순회--')

inorder(root)
print()
print('--후위순회--')

postorder(root)