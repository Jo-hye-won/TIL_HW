import sys
sys.stdin = open('input.txt')


def permutation(n, acc):
    global result
    if acc <= result:
        return
    if n == N:
        if acc > result:
            result = acc
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                permutation(n+1, acc * arr[n][i]*0.01)
                visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [0] * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    result = 0
    permutation(0, 1)
    print(f'#{tc} {result:7f}')