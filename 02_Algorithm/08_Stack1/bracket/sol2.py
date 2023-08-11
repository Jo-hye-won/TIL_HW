import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    case = list(input())
    stack = []
    for i in case:
        if i == "{" or i  == "(":
            stack.append(i)

        if i == "}" :
            if stack and stack[-1] =="{":
                stack.pop()
            else:
                stack.append(i)

        if i == ")":
            if stack and stack[-1] =="(":
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} -1')