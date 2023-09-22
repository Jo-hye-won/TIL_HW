import sys
sys.stdin = open('input.txt')

def perm(r, acc):
    global result
    if acc <= result:
        return
    # 종료 시점
    if r == N:
        if acc > result:
            result = acc
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                perm(r+1, acc * arr[r][i])
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         arr[i][j] /= 100
    #
    visited = [0] * N
    # 비교 대상군 -> 0 ( 최댓값을 구할 것이기 때문에, 점점 커질듯)
    result = 0
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    print(arr)
    perm(0, 1)
    # print(result)
    result = result*100
    print(f'#{tc} {result:7f}')