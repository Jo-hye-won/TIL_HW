import sys
sys.stdin = open('input.txt')

T = 10
W = 100

for tc in range(1, T+1):
    dump_count = int(input())
    dumps = list(map(int,input().split()))

    result = 0
    while dump_count >0:
        dump_count -= 1
        min_idx = 0
        max_idx = 0
        for i in range(1, W):
            if dumps[min_idx] > dumps[i]:
                min_idx = i
            if dumps[max_idx] <= dumps[i]:
                max_idx = i
        if dumps[max_idx] - dumps[min_idx] <= 1:
            result = dumps[max_idx] - dumps[min_idx]
            break
        else:
            dumps[max_idx] -= 1
            dumps[min_idx] += 1

    if dump_count == 0:
        min_idx = 0
        max_idx = 0
        for i in range(1, W):
            if dumps[min_idx] > dumps[i]:
                min_idx = i
            if dumps[max_idx] <= dumps[i]:
                max_idx = i
        result = dumps[max_idx] - dumps[min_idx]

    print(f'#{tc} {result}')
