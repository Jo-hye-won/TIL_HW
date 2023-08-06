import sys
sys.stdin = open('input.txt')

T = int(input())
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ''' 
     print(arr)
[[45, 15, 10, 56, 23], 
[96, 98, 99, 40, 69], 
[96, 84, 49, 46, 34], 
[16, 64, 81, 4, 11], 
[10, 66, 85, 55, 14]]
[[44, 91, 64, 73, 62], 
[78, 72, 52, 73, 48], 
[44, 88, 55, 75, 24], 
[22, 72, 59, 26, 62], 
[87, 11, 64, 79, 40]]
[[10, 10, 10, 10, 10], 
[10, 10, 10, 10, 10], 
[10, 10, 10, 10, 10],
[10, 10, 10, 10, 10], 
[10, 10, 10, 10, 10]]

    '''
    total = 0
        # 위  오  아  왼
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            center = arr[i][j]
            for k in range(4):
                ai = i + di[k]
                aj = j + dj[k]
                if 0 <= ai < N and 0 <= aj < N:
                    result = abs(center-arr[ai][aj])
                    total += result
    print(f'#{tc} {total}')
