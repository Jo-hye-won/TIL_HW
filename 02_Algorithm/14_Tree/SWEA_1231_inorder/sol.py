import sys
sys.stdin = open('input.txt')

# 중위순회
def inorder(p,N): # N : 완전이진트리의 마지막 정점
    if p <= N:
        inorder(p*2, N) # 왼쪽자식
        print(tree[p], end='') # 중위순회에서 할 일
        inorder(p*2+1, N)     # 오른쪽자식

    # if node != 0:
    #     inorder(left[node])  # 왼쪽 자식
    #     print(node, end=' ')
    #     inorder(right[node])

for tc in range(1, 11):
    N = int(input())  # 트리가 갖는 정점의 수
    tree = [0] * (N+1) # N번 노드까지 있는 완전 이진트리

    # # 왼쪽자식, 오른쪽자식, 부모정보
    # left = [0] * (N+1)
    # right = [0] * (N+1)
    # parent = [0] * (N+1)
    # words = [0] * (N+1)

    for i in range(N):
        # nodes = list(map(str, input().split()))
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위순회
    print(f'#{tc}', end=' ')
    inorder(1, N) # root = 1
    print()

    #     # words의 첫번째 인덱스에
    #     # 1인덱스위치의 단어 저장
    #     words[int(nodes[0])] = nodes[1]
    #     if len(nodes) == 3:
    #         left[int(nodes[0])] = int(nodes[2])
    #         parent[int(nodes[2])] = int(nodes[0])
    #     elif len(nodes) == 4:
    #         left[int(nodes[0])] = int(nodes[2])
    #         parent[int(nodes[2])] = int(nodes[0])
    #         right[int(nodes[0])] = int(nodes[3])
    #         parent[int(nodes[3])] = int(nodes[0])
    # inorder(1)