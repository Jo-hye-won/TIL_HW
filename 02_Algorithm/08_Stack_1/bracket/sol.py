import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sample = ['(', ')']
    gualhos = list(input())
    # print(gual)
    stack = []
    cnt = 0
    for i in sample:
        for j in gualhos:
            if i == j:
                stack.append(j)
                cnt += 1
    # print(len(stack))
    # print(cnt)
    if cnt % 2 == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} -1')
    # print(stack)
    # print(stack[-1])
    #     p = stack.pop()
    #     if  == "(":




    # stack.append(input())
    #
    # stack.append('A')
    # print(stack)
    # print(stack[-1])
    # print(stack.pop())