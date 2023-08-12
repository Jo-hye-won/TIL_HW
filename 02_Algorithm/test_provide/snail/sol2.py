T = int(input())

for test in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]  # NxN 행렬

    di = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 움직이는 방향
    idx = 0
    wall = [N - 1, N - 1, 0, 1]  # 벽에 해당하는 인덱스, 돌면서 한 칸씩 안쪽으로 좁혀짐
    i, j = 0, 0
    for n in range(1, N * N + 1):
        arr[i][j] = n

        i += di[idx][0]
        j += di[idx][1]

        if idx % 4 in [0, 2] and j == wall[idx]:
            wall[idx] -= di[idx][1]
            idx += 1
            idx %= 4

        elif idx % 4 in [1, 3] and i == wall[idx]:
            wall[idx] -= di[idx][0]
            idx += 1
            idx %= 4

    print(f'#{test}')
    for n in range(N):
        print(*arr[n])