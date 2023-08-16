import sys
sys.stdin = open('input.txt')

def search(now, acc):
    global result
    if acc > result:
        return
    if now == N:
        if acc < result:
            result = acc
    else:
        for row in range(N):  # 열증가
            if visited[row] == 0:
                visited[now] = 1
                search(now+1, acc + arr[now][row])
                visited[now] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N
    visited = [0] * N
    search(0, 0)
    print(f'#{tc} {result}')