import sys
sys.stdin = open('input.txt.py')

T = int(input())

for tc in range(1, T+1):
    M = input()     # str1
    N = input()     # str2
    # print(M ,N)
    # cnt = 0
    while 0 < len(M) and 0 < len(N):
        if M[i]
    # if M in N:
    #     cnt += 1
    # 이거 쓰지 말고 해봐

    # print(f'#{tc} {cnt}')

def func(P, T):
    p, t = len(P), len(T)
    i, j = 0, 0
    while i<t and j<p:
        if T[i] != P[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == p:
        return 1
    return 0

TC = int(input())
for tc in range(TC):
    P = input()
    T = input()
    print(f'#{tc+1} {func(P, T)}')