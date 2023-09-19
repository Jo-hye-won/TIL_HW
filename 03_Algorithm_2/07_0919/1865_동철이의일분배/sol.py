import sys
sys.stdin = open('input.txt')


def permutation(r, acc):
    global result
    if acc <= result:
        return
    # 종료 시점
    if r == N:
        if acc < result:
            # 그 값이 최솟값
            result = acc
        return
    else:
        # 모든 공장이 하나씩은 만들어야하니
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                # A 공장의 1번 제품 생산비용을 acc에 누적 해본다음
                permutation(r+1, acc*(arr[r][i])*0.01)
                # A 공장이 1번 제품을 안쓰고, 2번 제품을 썼을 때
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    visited = [0] * N
    # 비교 대상군
    result = sum(sum(arr, []))
    permutation(0, 1)
    print(result)
