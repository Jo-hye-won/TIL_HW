import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    benefit = 0

    G = N//2
    for i in range(N):
        if i <= G:
            for j in range(G-i, G+i+1):
                benefit += arr[i][j]
        else:
            for j in range(i-G, N-i+G):
                benefit += arr[i][j]
    print(f'#{tc} {benefit}')