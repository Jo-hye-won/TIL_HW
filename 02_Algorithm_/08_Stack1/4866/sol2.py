import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []      # 빈스택 만들기
    sentence = input()  # 문자열 리스트로 받아오기
    # print(sentence)
    for i in sentence:
        if i == "(" or i == "{":
            stack.append(i)
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        if i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:   # stack = []
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')