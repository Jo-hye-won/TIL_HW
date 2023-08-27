import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    mx = 0
    for i in range(N-2): # 범위 3개로 나누기 위해서 N-2
        for j in range(i+1, N-1): # 중간 범위
            cnt = 0
            for s in range(i+1): # 처음 범위
                cnt += arr[s].count('W') # W의 개수
            for s in range(i+1, j+1):
                cnt += arr[s].count('B') # B의 개수
            for s in range(j+1, N):
                cnt += arr[s].count('R') # R의 개수
            mx = max(mx, cnt)
    print(f'#{tc} {N*M-mx}')