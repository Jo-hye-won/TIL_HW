import sys
sys.stdin = open('view.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    h = list(map(int, input().split()))
    res = 0
    for i in range(2, N-2):
        a = h[i] - h[i+1]
        b = h[i] - h[i+2]
        c = h[i] - h[i-1]
        d = h[i] - h[i-2]
        if a > 0 and b > 0 and c > 0 and d > 0:
            res += min(a,b,c,d)
    print(res)