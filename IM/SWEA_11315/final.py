import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    success = 5
    omok = [list(input()) for _ in range(N)]
    # print(omok)

    # garo
    result = 'NO'
    for i in range(N):
        five = 0
        for j in range(N):
            if omok[i][j] == 'o':
                five += 1
            if omok[i][j] == '.':  # .을 만나면 five값 0으로 초기화 되야 한다
                five = 0
            if five >= success:
                result = 'YES'

    # sero
    for i in range(N):
        five1 = 0
        for j in range(N):
            if omok[j][i] == 'o':
                five1 += 1
            if omok[j][i] == '.':
                five1 = 0
            if five1 >= success:
                result = 'YES'

    for i in range(N):
        five2 = 0
        for j in range(N):
            if omok[i][j] == 'o':
                five2 = 1
                for x in range(1, 5):
                    if i+x < N and j + x < N and omok[i+x][j+x] == 'o':
                        five2 += 1
                        if five2 == success:
                            result = 'YES'

    for i in range(N):
        five3 = 0
        for j in range(N):
            if omok[i][j] == 'o':
                five3 = 1
                for x in range(1, 5):
                    if i+x < N and j-x < N and omok[i+x][j-x] == 'o':
                        five3 += 1
                        if five3 == success:
                            result = 'YES'

    print(f'#{tc} {result}')