import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node != 0:
        inorder(left[node])  # 왼쪽 자식
        print(node, end=' ')
        inorder(right[node])

for tc in range(1, 11):
    N = int(input())
    # 왼쪽자식, 오른쪽자식, 부모정보
    left = [0] * (N+1)
    right = [0] * (N+1)
    parent = [0] * (N+1)
    words = [0] * (N+1)

    for i in range(N):
        nodes = list(map(str, input().split()))
        # words의 첫번째 인덱스에
        # 1인덱스위치의 단어 저장
        words[int(nodes[0])] = nodes[1]
        if len(nodes) == 3:
            left[int(nodes[0])] = int(nodes[2])
            parent[int(nodes[2])] = int(nodes[0])
        elif len(nodes) == 4:
            left[int(nodes[0])] = int(nodes[2])
            parent[int(nodes[2])] = int(nodes[0])
            right[int(nodes[0])] = int(nodes[3])
            parent[int(nodes[3])] = int(nodes[0])
    inorder(1)