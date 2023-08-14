import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cal = input()
    result = ''
    stack = []
    for char in cal:
        if char not in '+*':
            stack.append(char)   # 숫자는 스택에 넣는다.
        elif char in '+':
            b = int(stack.pop())
            a = int(stack.pop())
            re = a + b
            stack.append(re)
        elif char in '*':
            b = int(stack.pop())
            a = int(stack.pop())
            re = a * b
            stack.append(re)
            print(stack)