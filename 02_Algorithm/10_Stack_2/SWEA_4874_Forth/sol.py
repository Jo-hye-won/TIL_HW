import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cal = input().split()
    result = ''
    stack = []
    top = -1
    for char in cal:
        if char not in '+-*/.':  # 연산자가 아니면(숫자이면)
            stack.append(int(char))   # 숫자는 스택에 넣는다.
        elif char == '.':   # 그런데 .이면
            if len(stack) == 1:
                print(f'#{tc} {stack[top]}')
            else:
                print(f'#{tc} error')

        elif len(stack) > 1:  # stack에 값이 2개 이상 존재하면
            b = stack.pop()  # 연산할 뒤에꺼부터 꺼내야 함
            a = stack.pop()
            if char == '+':
                stack.append(a+b)   # 더해서 집어넣기
            elif char == '*':
                stack.append(a*b)   # 곱해서 집어넣기
            elif char == '-':
                stack.append(a-b)   # 빼고 집어넣기
            elif char == '/':
                stack.append(int(a/b))   # 노나서 집어넣기
        else:
            print(f'#{tc} error')
            break




    # if len(stack) >= 2:   # 스택에 숫자만 2개 이상이 남아있으면 연산 불가
    #     print('error')
    # else:
    #     print(f'#{tc} {stack[top]}')