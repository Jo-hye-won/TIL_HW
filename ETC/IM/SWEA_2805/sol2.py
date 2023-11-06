import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    result = 0

    M = N // 2
    for i in range(N):
        if i <= M:
            for j in range(M-i, M+i+1):
                result += arr[i][j]
        else:
            for j in range(i-M, N-(i-M)):
                result += arr[i][j]

    print(f'#{tc} {result}')