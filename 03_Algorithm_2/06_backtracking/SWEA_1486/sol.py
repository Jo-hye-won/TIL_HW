import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    Hs = list(map(int, input().split()))

    small = 987654321
    for n in range(1, N+1):
        for tu in combinations(Hs, n):
            sum_tu = sum(tu)
            if sum_tu >= B:
                compare = sum_tu - B
            # elif:
            #     continue
                if small >= compare:
                    small = compare

    print(f'#{tc} {small}')


    #     A = combinations(Hs, 1)
    # B = combinations(Hs, 2)
    # C = combinations(Hs, 3)
    # print(ls)

    #
    # print(f'#{tc} {result}')