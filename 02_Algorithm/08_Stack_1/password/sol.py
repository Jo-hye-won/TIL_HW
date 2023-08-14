import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, S = input().split()  # 10, 123809~
    # print(N,S)  문자열이 저기 들어갈 수 없네
    stack = []  # ['1','2','3','4']
    for i in range(int(N)):  # 10번 돌면서  # 0
        if stack:  # 스택에 값이 있다면
            # S의 i번째 문자가 스택의 마지막에 넣은 값이랑 같으면
            if S[i] == stack[-1]:
                stack.pop()  # 추출
            else:   # 일치 하지 않으면
                stack.append(S[i])     # 추가
        else:   # 스택에 값이 없으면
            stack.append(S[i])     # 값 추가 #1
    # print(stack)
    print(f'#{tc}',end=' ')
    for j in stack:
        print(j, end='')
    print()
