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
            multis.append(str(multi))

    danjo = []
    for k in multis:
        LEN = len(k)
        if LEN < 2:
            continue
        # print(k)
        # if LEN >= 2:
            # for l in range(LEN):
        check = True
        for a in range(LEN-1):
            if k[a] > k[a+1]:
                check = False
                break
        if check:
            danjo.append(int(k))

    # print(danjo)
    result = max(danjo)
    if danjo:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')