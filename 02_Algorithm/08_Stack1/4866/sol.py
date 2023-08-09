
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    stack = []      # 빈스택 만들기
    sentence = list(input())  # 입력값 받아오기
    for i in sentence:  # 입력값의 인자들 하나씩 순회하기
        if i == "(" or i == "{":    # 불러온 값이 (이거나 {이면
            print(stack)
            stack.append(i)  # 스택에 추가해주고
        if i != "(":    # ( 아니면
            continue    # 그냥 지나가
        if i != "{":  # { 아니면
            continue  # 그냥 지나가
        if i == ")" and stack[-1] == "("
    print(stack)

    #
    # if len(stack) == 0:
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')