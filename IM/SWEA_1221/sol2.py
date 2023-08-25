import sys
sys.stdin = open('input.txt')

A = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for tc in range(1, T+1):
    _, N = input().split()
    lst = list(input().split())

    num_lst = []
    for i in range(int(N)):
        num_lst.append(A.index(lst[i]))
    num_lst.sort()

    for j in range(len(num_lst)):
        num_lst[j] = A[num_lst[j]]

    print(f'#{tc}')
    print(*num_lst)