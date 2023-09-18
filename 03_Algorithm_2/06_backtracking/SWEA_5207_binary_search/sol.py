import sys
sys.stdin = open('input.txt')


def binary_search(L, R, K, D):
    global result
    mid = (L + R) // 2
    if A[mid] == K:
        result += 1
        return
    elif A[mid] < T:
        if D == 'right':
            return
        binary_search(mid+1, R, K, 'right')
    else:
        if D == 'left':
            return
        binary_search(L, mid-1, K, 'left')




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    for idx in range(M):
        binary_search()
