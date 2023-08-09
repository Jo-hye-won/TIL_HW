import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    case = list(input())
    stack = []
    for i in case:
        if i == "{":
            stack.append(i)
        if i == "(":
            stack.append(i)
        else:
            if stack[-1] == "{" or stack[-1] == "(":
                stack.pop()
        print(stack)