import sys
sys.stdin = open('input.txt')
from collections import deque

'''
M번까지 M개의 피자를 순서대로 화덕에 넣을 때,
화덕에 마지막 까지 남아있는 피자 번호를 알아내라
'''
T = int(input())

def pizza_fired(que):
    first = que.popleft()
    re = int(first) // 2
    if re != 0:
        que.append(str(re))
    return que


for tc in range(1, T+1):
    N, M = map(int, input().split())   # N = 화덕의 크기, M = 피자 개수
    C = input().split()  # 이케하면 리스트로 받아와진다.
    que = deque(C)
    where_pizza = []
    idx = 1
    # 언제까지 피자를 구워야 할까??? 하나 남았을 때까지
    while que:
        pizza_fired(que)
        where_pizza.append(idx)
        idx += 1
        # if que.popleft() == 0:


# if que.popleft() == 0:

# print(que)
# for pizza in zip(que):
#     if sum(piz)
# while que.popleft() > 0: