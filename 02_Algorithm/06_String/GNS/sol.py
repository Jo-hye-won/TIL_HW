import sys
sys.stdin = open('input.txt')

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(T):
    tn, N = map(str,input().split())
    # t, N = map(str, input().split())
    # N = int(N)
    arr = list(map(str, input().split()))
    # print(arr)
    tmp = [0]*10

    for i in range(len(numbers)):
        for j in range(tmp[i]):
            if arr[j] == numbers[i]:
                tmp[i] += 1

    print(f'#{tc}')
#
    for j in range(10):
        for k in range(tmp[j]):
            print(numbers[j], end=' ')

    print(numbers)