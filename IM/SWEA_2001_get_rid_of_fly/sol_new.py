import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split()))for _ in range(N)]

    max_die = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    result += flies[k][l]
            if max_die < result:
                max_die = result
    print(f'#{tc} {max_die}')


