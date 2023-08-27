import sys
sys.stdin = open('sumo.txt')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    numbers = list(input().split())
    # print(numbers)

    # max_sums = 0
    # min_sums =

    for i in range(N-M+1):   # i위치에서 M개의 원소를 더해서 비교해야하기 때문에 범위 -M 해주기
        sums = 0
        for j in range(M):   # 구간합 구하기위한 범위
            sums += int(numbers[i+j])  # i에서 시작하는 구간의 각 원소 sums에 더해서 구간 합 구하기

        if i == 0:
            max_sums,min_sums = sums, sums
        else:
            if max_sums < sums:   # 구간합이 최대값으로 설정해 둔 것보다 크면
                max_sums = sums     # 구간합으로 최대값 변경 반복
            if min_sums > sums:   # 구간합이 최소값으로 설정해 둔 것보다 작으면
                min_sums = sums     # 구간합으로 최소값 변경 반복


    result = max_sums - min_sums
    print(f'#{tc} {result}')



# print(sum_M,'numbes리스트에서 M개씩 더한 값을 sum_M리스트에 담아주기')

# 더한 값들 중에서 최대, 최소값 찾기
#
#     for k in sum_M:
#         if max_sums < sum_M[k]:
#             max_sums = sum_M[k]
#         if min_sums > sum_M[k]:
#             min_sums = sum_M[k]
#     print(sum_M)

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
money_cnt = [0] * 8

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for i in range(8):
        # money의 각 금액으로 나눈 몫이
        # 그 돈을 사용할 개수가 되고
        # 나머지로 다시 또 다른 금액이 몇개 필요한지 반복해야한다
        money_cnt[i] = N // money[i]
        N %= money[i]
    print(f'#{tc}')
    print(*money_cnt)