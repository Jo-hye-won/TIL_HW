import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_die = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            point = 0  # 다 더한값 구하기 위해서 초기값 설정
             # 이건 point = arr[i][j]이렇게 하면 안됨
            for k in range(i, i+M):
                for l in range(j, j+M):
                    point += arr[k][l]
            if max_die <= point:
                max_die = point
    print(f'#{tc} {max_die}')