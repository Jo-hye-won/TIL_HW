import sys
sys.stdin = open('input.txt')

# def back(sentence, result):

T = int(input())
for tc in range(1, T+1):
    sentence = input()
    result = ''
    stack = []
    # back(sentence, result)
    for i in sentence:
        if i not in '+-*/':
            result += i
        else:
            stack.append(i)
    while stack:
        result += stack.pop()
        # return result

    print(f'#{tc} {result}')