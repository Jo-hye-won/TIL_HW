import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    words = input()
    for i in words:
        if len(stack) == 0:
            stack.append(i)    # A
        else:
            if stack[-1] == i:  # 위에 if문 이미 한 후이기 때문에 다음 값이 i에 들어와있다.
                stack.pop()
            else:
                stack.append(i)

    print(f'#{tc}', len(stack))