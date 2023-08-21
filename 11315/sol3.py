def check(row, col, di, dj):
    cnt = 0
    while 0 <= row < N and 0 <= col < N and pan[row][col] == 'o':
        cnt += 1
        row += di
        col += dj
    return cnt >= 5  # 연속된 'o'의 개수가 5 이상이면 True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pan = [list(input()) for _ in range(N)]
    res = 'NO'

    for i in range(N):
        for j in range(N):
            # 가로 확인
            if check(i, j, 0, 1):
                res = 'YES'

            # 세로 확인
            if check(i, j, 1, 0):
                res = 'YES'

            # 대각선 ( 오른쪽 아래 ) 확인
            if check(i, j, 1, 1):
                res = 'YES'

            # 대각선 ( 왼쪽 아래 ) 확인
            if check(i, j, 1, -1):
                res = 'YES'
    print(f'#{tc} {res}')