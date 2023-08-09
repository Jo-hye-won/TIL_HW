import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    st = list(input())
    # print(st)
    N = len(st)
    for i in range(N//2):
        st[i], st[N-1-i] = st[N-1-i], st[i]
    print(f'#{tc}',''.join(st))