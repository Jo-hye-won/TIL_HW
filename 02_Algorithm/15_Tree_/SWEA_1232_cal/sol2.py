import sys

sys.stdin = open('input.txt')


# 후위 순회
def postorder(p, N):
    if p <= N:
        postorder(p*2, N)
        postorder(p*2+1, N)
        stack.append(tree[p])

T = 10
for tc in range(1, T+1):
    N = int(input()) # 정점의 개수
    tree = [0] * (N+1)
    stack = []

    for i in range(N):
        arr = list(input().split())
        # print(arr)
        tree[int(arr[0])] = arr[1]

    for num in stack:
        if num not in '+-*/()':
            stack.append(int(num))
        else:
            b = stack.pop()
            a = stack.pop()
            if num == '+':
                stack.append(a+b)
            elif num == '-':
                stack.append(a - b)
            elif num == '*':
                stack.append(a * b)
            elif num == '/':
                stack.append(a / b)

        print(f'#{tc} {stack[-1]}')

# arr = []
# for i in data:
#     if i.isdigit():
#         arr.append(int(i))
#     else:
#         arr.append(i)
