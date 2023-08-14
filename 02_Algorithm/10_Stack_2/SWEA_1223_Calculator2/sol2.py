# 후위 표기식으로 바꾸기
def to_postfix(fx):
    s = ''
    stack = []
    for char in fx:
        if char not in '+*':
            s += char
        elif char == '*':
            while stack and stack[-1] == '*':
                s += stack.pop()
            stack.append(char)
        elif char == '+':
            while stack:
                s += stack.pop()
            stack.append(char)
    while stack:  # stack에 남아있는 애들 마지막으로 적어줘야함
        s += stack.pop()
        # print(s)
    return s


def cal(s):
    stack = []
    for char in s:
        if char not in '+*':
            stack.append(char)
        elif char == '+':
            op1 = int(stack.pop())  # 형변환 해줘야함을 유의
            op2 = int(stack.pop())
            stack.append(op2 + op1)  # chr 아님을 유의
        elif char == '*':
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            stack.append(op2 * op1)
        # print(stack)
    return stack[0]


for tc in range(1, 11):
    len_fx = int(input())
    fx = input()
    s = to_postfix(fx)
    # print(s)
    print(f'#{tc} {cal(s)}')