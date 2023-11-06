import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    non = [list(map(int, input())) for _ in range(N)]

    result = 0
    point = N//2

    for i in range(N):
        if i <= point:
            for j in range(point-i, point+i+1):
                result += non[i][j]
        else:
            for j in range(i-point, N-(i-point)):
                result += non[i][j]
    print(f'#{tc} {result}')

