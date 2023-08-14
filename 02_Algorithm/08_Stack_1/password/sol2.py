import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, S = input().split()
    stack =[]
    for i in range(int(N)):
        if len(stack) == 0:
            stack.append(S[i])
        else:
            if S[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[i])
    print(f'#{tc}', end=' ')
    for j in stack:
        print(j, end='')
    print()