import sys
sys.stdin = open('input.txt')
#
#      # 상 하 좌 우
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_die = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            res = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    res += arr[k][l]
            if max_die <= res:
                max_die = res
    print(f'#{tc} {max_die}')
