import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    multis = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            multi = numbers[i]*numbers[j]
            multi_list = list(map(int, str(multi)))
            multi_len = len(multi_list)
            # print(multi_list)  # [8] / [1, 4] / [2, 0] / [2, 8] / [4, 0] / [7, 0]
            check = True
            for a in range(multi_len - 1):
                if multi_list[a] > multi_list[a+1]:
                    check = False
                    break
            else:
                multis.append(multi)

    result = int(max(multis))
    if multis:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')








    # danjo = []
    #
    # for k in multis:
    #     if len(k) >= 2:
    #         for l in range(len(k)):
    #             for a in range(len(k)-1):
    #                 if k[a] <= k[a+1]:
    #                     danjo.append(k)
    #
    # print(danjo)
    # result = max(danjo)
    # print(f'#{tc} {result}')
