import sys
sys.stdin = open('input.txt')

def inorder(node):
    global count
    if node <= N:
        # 왼쪽자식
        inorder(node*2)
        # 트리에 값 할당
        tree[node] = count
        count += 1
        inorder(node*2 + 1)




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # root를 1로 한다
    # tree를 그릴 때, 0번은 쓰지 않는다.
    # N 노드의 개수
    # Tree N+1 만큼 담을 수 잇어야 한다
    tree = [0] * (N+1)
    # 입력할 값
    count = 1
    inorder(1)

    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')