import sys
sys.stdin = open('sumo.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    ls = []
    # max_sum = min_sum = 0
    for i in range(N-M+1):
        num_sum = numbers[i]
        for j in range(i+1, M+i):
            num_sum += numbers[j]
        ls.append(num_sum)
    # print(ls)
    max_sum = ls[0]
    min_sum = ls[0]
    for k in ls:
        if max_sum <= k:
            max_sum = k
        if min_sum >= k:
            min_sum = k
    ans = max_sum - min_sum
    # print(max_sum, min_sum)

    print(f'#{tc} {ans}')