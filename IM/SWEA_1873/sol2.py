import sys
# sys.stdin = open('question.txt')

T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    N = int(input())
    comm = input()

    for i in range(H):
        for j in range(W):
            if MAP[i][j] in '<>^v':
                row = i
                col = j
                break

    for i in range(len(comm)):
        t_row = row
        t_col = col

        if comm[i] == 'U':
            MAP[t_row][t_col] = '^'
            if t_row-1 >= 0 and MAP[t_row-1][t_col] == '.':
                MAP[t_row-1][t_col] = '^'
                MAP[t_row][t_col] = '.'
                row -= 1

        elif comm[i] == 'R':
            MAP[t_row][t_col] = '>'
            if t_col+1 < W and MAP[t_row][t_col+1] == '.':
                MAP[t_row][t_col+1] = '>'
                MAP[t_row][t_col] = '.'
                col += 1

        elif comm[i] == 'L':
            MAP[t_row][t_col] = '<'
            if t_col -1 >= 0 and MAP[t_row][t_col-1] == '.':
                MAP[t_row][t_col-1] = '<'
                MAP[t_row][t_col] = '.'
                col -= 1

        elif comm[i] == 'D':
            MAP[t_row][t_col] = 'v'
            if t_row+1 < H and MAP[t_row+1][t_col] == '.':
                MAP[t_row+1][t_col] = 'v'
                MAP[t_row][t_col] = '.'
                row += 1

        elif comm[i] == 'S':
            if MAP[t_row][t_col] == '^':
                if t_row -1 >= 0:
                    for u in range(t_row-1, -1, -1):
                        if MAP[u][t_col] == '*':
                            MAP[u][t_col] = '.'
                            break
                        elif MAP[u][t_col] == '#':
                            break

            elif MAP[t_row][t_col] == '>':
                if t_col + 1 < W:
                    for r in range(t_col + 1, W):
                        if MAP[t_row][r] == '*':
                            MAP[t_row][r] = '.'
                            break
                        elif MAP[t_row][r] == '#':
                            break

            elif MAP[t_row][t_col] == 'v':
                if t_row + 1 < H:
                    for d in range(t_row +1, H):
                        if MAP[d][t_col] == '*':
                            MAP[d][t_col] = '.'
                            break
                        elif MAP[d][t_col] == '#':
                            break

            elif MAP[t_row][t_col] == '<':
                if t_col - 1 >= 0:
                    for l in range(t_col - 1, -1, -1):
                        if MAP[t_row][l] == '*':
                            MAP[t_row][l] = '.'
                            break
                        elif MAP[t_row][l] == '#':
                            break


    print(f'#{tc} {"".join(MAP[0])}')
    for k in range(1, H):
        print("".join(MAP[k]))