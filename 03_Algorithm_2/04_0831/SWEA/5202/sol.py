import sys
sys.stdin = open('input.txt')

import itertools

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    SE = [list(map(int, input().split())) for _ in range(N)]
    result = 1
    # print(list(itertools.permutations(SE)))
    SE.sort(key=lambda x: x[1])
    # print(SE)

    # 1. 앞에 작업하는 애가 끝나야 내가 시작할 수 있다.
    # 2. 어떻게든 최대한 많이 우겨 넣을거다.
    # 3. 최대한 앞에서부터 채워나가서 많이 채울 수 있는 방법을 볼거다.
    end_time = SE[0][1]
    for i in range(1, N):
        if end_time <= SE[i][0]:
            result += 1
            end_time = SE[i][1]
    print(f'#{tc} {result}')

