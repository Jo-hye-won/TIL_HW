import sys
sys.stdin = open('sumo.txt')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    numbers = list(input().split())
    # print(numbers)

    sums_ls =[]
    for i in range(N-M+1):   # i위치에서 M개의 원소를 더해서 비교해야하기 때문에 범위 -M 해주기
        sums = 0
        for j in range(M):   # 구간합 구하기위한 범위
            sums += int(numbers[i+j])  # i에서 시작하는 구간의 각 원소 sums에 더해서 구간 합 구하기
        # print(type(sums))
        sums_ls.append(sums)
    # print(sums_ls)

    for bubble in range(len(sums_ls)-1, 0, -1):
        for k in range(bubble):
            if sums_ls[k] > sums_ls[k+1]:
                sums_ls[k], sums_ls[k + 1] = sums_ls[k+1], sums_ls[k]
    # print(sums_ls)

    result = sums_ls.pop()-sums_ls.pop(0)
    print(f'#{tc} {result}')