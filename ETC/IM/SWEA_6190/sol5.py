import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    multis = []
    for i in range(N):
        for j in range(i+1, N):
            multi = numbers[i]*numbers[j]
            multis.append(str(multi))

    danjo = []
    for k in multis:
        LEN = len(k)
        if LEN < 2:
            continue

        check = True
        for a in range(LEN-1):
            if k[a] > k[a+1]:
                check = False
                break
        if check:
            danjo.append(int(k))

    if danjo:
        result = max(danjo)  # max doesn't work in empty list
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')