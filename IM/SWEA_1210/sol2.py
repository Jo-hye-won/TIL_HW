for tc in range(1, 11):
    _ = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점인 2를 찾는 함수 없이 직접 도착지점의 x,y 좌표를 찾기
    for i in range(100):
        if ladders[99][i] == 2:
            y = i
            break

    x = 99
    while x > 0:
        # 왼쪽으로 이동할 수 있으면 이동
        if y > 0 and ladders[x][y-1] == 1:
            while y > 0 and ladders[x][y-1] == 1:
                y -= 1

        # 오른쪽으로 이동할 수 있으면 이동
        elif y < 99 and ladders[x][y+1] == 1:
            while y < 99 and ladders[x][y+1] == 1:
                y += 1

        x -= 1  # 위로 이동

    print(f'#{tc} {y}')