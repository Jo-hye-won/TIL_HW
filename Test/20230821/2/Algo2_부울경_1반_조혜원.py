import sys
sys.stdin = open('algo2_sample_in.txt')

'''
M번째로 카드를 가져갈 때 얻을 수 있는 점수는 몇점인가?

카드덱 A : N장의 카드, 숫자 또는 '+'가 적혀있음
카드덱 B : 홀수카드만 놓을 수 있고, 선입선출 방식
카드덱 C : 짝수카드만 놓을 수 있고, 후입선출 방식
더하기카드 : 보너스 숫자 1증가 (0부터 시작해서 + 만날때마다 1씩 증가)

게임 참가자의 수 = 최대 10명

카드덱 A에 
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cards = input().split()
    # print(cards)
    B_que = []  # 선입선출방식 que.pop(0)
    C_stack = [] # 후입선출방식 stack.pop()
    bonus = ''
    # for n in N:

    for i in cards:
        if i == '+':
            i = 0 # 보너스 숫자는 0부터 시작
            # i += 1 # +카드 만날 때마다 1씩 증가
        if int(i) % 2 == 0:  # 짝수면
            C_stack.append(i)   # 스택에 넣고
        if int(i) % 2 == 1: # 홀수면
            B_que.append(i) # 큐에넣고
    print(B_que)
    print(C_stack)
    # for n in range(10):
    #     if n ==