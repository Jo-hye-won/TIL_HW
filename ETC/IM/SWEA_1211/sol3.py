for tc in range(1, 11):
    input()
    MAP = [list(map(int, input().split())) for _ in range(100)]

    MIN = float('inf')
    res = -1
    for start in range(100):
        if MAP[0][start] == 1:
            col = start
            row = 0
            cnt = 0

            while row < 99:
                cnt += 1

                # 오른쪽으로 이동
                if col < 99 and MAP[row][col+1] == 1:
                    while col < 99 and MAP[row][col+1] == 1:
                        col += 1
                        cnt += 1
                # 왼쪽으로 이동
                elif col > 0 and MAP[row][col-1] == 1:
                    while col > 0 and MAP[row][col-1] == 1:
                        col -= 1
                        cnt += 1
                row += 1
            if MIN > cnt:
                MIN = cnt
                res = start
    print(f'#{tc} {res}')