
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    stack = []      # 빈스택 만들기
    sentence = list(input())  # 문자열 리스트로 받아오기
    # print(sentence)
    N = len(sentence)   # 리스트의 길이받아서
    for i in range(N):  # 길이만큼 순회하자
        # for j in ra

        # i인덱스위치의 값이 (이거나 {이면
        if sentence[i] == "(" or sentence[i] == "{":
            # print(stack)
            stack.append(i)  # 스택에 추가해주고

        # if아니고 i 인덱스 위치의 값이 ) 이거나 } 이면 stack에 있는 값 pop하기
        elif sentence[i] == ")" or sentence[i] == "}":
            S = stack.pop()

            # sentence[i]의 값이 ")"이고 pop한 값이 "("이면 한 쌍이 됨
            if sentence[i] == ")" and S == "(":



    #     # print(stack)
    #
    #
    # if len(stack) == 0:
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')
