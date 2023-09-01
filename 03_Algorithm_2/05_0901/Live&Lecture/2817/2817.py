# 부분 수열의 합(2817)
'''
1
4 3
1 2 1 2

#1 4
'''

# sol 1 =============================================================
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0 # 합이 K가 되는 경우의 수
    for i in range(1 << N):   # 부분집합을 표시하는 i
                              # 비트검사를한 결과가 0이 아니면 그 원소가 포함된 경우
        s = 0                 # 부분집합의 합을 저장하기 위한 초기화
        for j in range(N):
            if i & (1 << j):  # i의 j번 비트 검사
                s += arr[j]   # 0이 아니면 j번 원소가 부분집합에 포함됨
        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')


# sol 2 =======================a===========================================
def f(i, N, s, K,rs):
    global cnt
    global call
    call += 1
    if i == N:
        if s == K:  # 너가 선택한 원소들의 합이 K랑 같으면
            cnt += 1
    elif s > K:  # 남은원소가 있으면 하나라도 포함시키면 커진다
        return
    elif s + rs < K:
        return

    else:
        f(i+1, N, s+arr[i], K, rs-arr[i])
        f(i+1, N, s, K, rs-arr[i])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    call = 0
    f(0, N, 0, K)
    print(f'#{tc} {cnt} {call}')