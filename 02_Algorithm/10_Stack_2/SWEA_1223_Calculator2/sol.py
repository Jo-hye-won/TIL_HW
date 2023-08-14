import sys
sys.stdin = open('input.txt')

T = 10
# 먼저 후위 표기식으로 바꾸자
for tc in range(1, T+1):
    lens = int(input())
    cal = input()
    result = ''
    stack =[]
    for char in cal:
        if char not in '+-*/()':  # 연산자가 아니면
            result += char      # result에 넣어주자
        elif char in '*/':
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)
        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        elif char in ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    while stack:
        result += stack.pop()
    # print(f'{tc} {result}')

# 후위 표기식으로 반환된 result를 계산하자
    susik = result
    top = -1
    for x in susik:
        if x not in '+-/*':  # x가 연산자가 아니면
            stack.append(int(x))  # 스택에 넣어주고 # x가 문자열 형태라서 연산하기 위해 형변환 int로 해주기
        else:       # x가 연산자면
            b = stack.pop()  # 스택에서 b랑 a 빼와서 계산해야지
            a = stack.pop()
            if x == '+':  # 더하기일 경우
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            elif x == '*':
                stack.append(a * b)
            elif x == '/':
                stack.append(a / b)

    print(f'#{tc} {stack[top]}')