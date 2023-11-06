import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[0]
    min_num = numbers[0]
    for i in numbers:
        if max_num <= i:
            max_num = i
        if min_num >= i:
            min_num = i
    chi = max_num - min_num
    print(f'#{tc} {chi}')
