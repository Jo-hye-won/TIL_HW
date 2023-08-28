import sys
sys.stdin = open('input.txt')
# numbers = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6,
# 'SVN':7, 'EGT':8, 'NIN':9}
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(1, T+1):
    tc, L = input().split()
    num_ls = list(input().split())
    # sort_ls = sorted(num_ls, reverse=True)
    ls = []
    N = len(num_ls)
    for i in range(N):
        ls.append(numbers.index(num_ls[i]))
    # print(ls)
    ls.sort()

    for j in range(N):
        ls[j] = numbers[ls[j]]

    print(tc)
    print(*ls)