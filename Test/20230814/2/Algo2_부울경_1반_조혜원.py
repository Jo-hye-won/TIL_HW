T = int(input())
for tc in range(1, T +1):
    sentence = input()
    stack = []
    result = 0
    gap = 1

    for i in sentence:
        # print(i)
        if i == '(':     # '('인 경우
            stack.append(i)  # 스택에 넣고
            # print(stack)
        if i == ')':  # 다음 올 값이 ')'이고
            if stack and stack[-1] == '(':  # 스택의 마지막값이 '('인경우
                stack.pop()  # 스택에서 빼자
            else:
                stack.append(i)
        if i == '{':
            stack.append(i)
        if i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        print(f'#{tc} 100')
    else:
        print(f'#{tc} -1')