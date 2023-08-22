import sys
sys.stdin = open('input.txt')


# 중위순회
def inorder(p, N): # N : 완전이진트리의 마지막 정점
    if p <= N:
        inorder(p*2, N)  # 왼쪽자식
        print(tree[p], end='')  # 중위순회에서 할 일
        inorder(p*2+1, N)     # 오른쪽자식


for tc in range(1, 11):
    N = int(input())  # 트리가 갖는 정점의 수
    tree = [0] * (N+1)  # N번 노드까지 있는 완전 이진트리

    for i in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위순회
    print(f'#{tc}', end=' ')
    inorder(1, N)   # root = 1
    print()