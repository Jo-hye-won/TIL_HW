# 사칙연산
import sys
sys.stdin = open('input.txt')

def postorder(n):
    if tree[n]: # 노드 n 비어있지 않으면
        if tree[n] == '+':
            return postorder(ch1[n]) + postorder(ch2[n])
        elif tree[n] == '-':
            return postorder(ch1[n]) - postorder(ch2[n])
        elif tree[n] == '*':
            return postorder(ch1[n]) * postorder(ch2[n])
        elif tree[n] == '/':
            return postorder(ch1[n]) / postorder(ch2[n])
        else: # 현재 노드가 숫자라면
            return int(tree[n])  # 해당 숫자 값을 반환
    else: # 노드 n이 비어있으면 (자식노드 없을때)
        return 0

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1) # 노드 연산자 또는 숫자 저장
    ch1 = [0] * (N + 1) # 왼쪽 자식
    ch2 = [0] * (N + 1) # 오른쪽 자식
    for i in range(N):
        lst = input().split()
        tree[int(lst[0])] = lst[1] # 노드에 연산자 또는 숫자 할당
        if len(lst) > 2:
            ch1[int(lst[0])] = int(lst[2])  # 왼쪽 자식노드 번호 할당
            ch2[int(lst[0])] = int(lst[3])  # 오른쪽 자식노드 번호 할당

    res = int(postorder(1))
    print(f'#{tc} {res}')