import sys
sys.stdin = open('input.txt')
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for _ in range(1, T+1):
    tc, N = map(str, input().split())
    arr = list(map(str, input().split()))
    # print(arr)
    length = int(N)

    result = []
    for i in range(10):
        cnt = 0
        for number in arr:
            if number == numbers[i]:
               cnt += 1
                # print(type(number))
        result += [numbers[i]] * cnt
    print(tc)
    print(*result)







