import sys
sys.stdin = open('input.txt')

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for tc in range(1, T+1):
    _, N = input().split()
    li = list(input().split())
    li1 = []
    for i in range(int(N)):
        li1.append(numbers.index(li[i]))
        # print(A.index(li[i]))
    li1.sort()
    # print(li1)
    #
    for i in range(int(N)):
        li1[i] = numbers[li1[i]]

        # print(li1[i])
    #
    print(f'#{tc}')
    print(*li1)