import sys
sys.stdin = open('input.txt')


# 중위 순회
def postorder(p, N):
    if p <= N:
        postorder(p*2, N)
        postorder(p*2+1, N)
        stack.append(tree[p])
    return stack


T = 10
for tc in range(1, T+1):
    N = int(input()) # 정점의 개수
    tree = [0] * (N+1)
    stack = []

    for i in range(N):
        arr = list(input().split())
        print(arr)
        tree[int(arr[0])] = arr[1]
    # print(tree)

    # print(f'#{tc}', end= ' ')
    postorder(1, N)
    # print()

    susik = postorder(1, N)
    print(susik)
    #
    # for x in susik:
    #     if x not in '+-*/()':
    #         stack.append(int(x))
    #     else:
    #         b = stack.pop()
    #         a = stack.pop()
    #         if x == '+':
    #             stack.append(a+b)
    #         elif x == '-':
    #             stack.append(a - b)
    #         elif x == '*':
    #             stack.append(a * b)
    #         elif x == '/':
    #             stack.append(a / b)
    # print(f'#{tc} {stack[-1]}')
