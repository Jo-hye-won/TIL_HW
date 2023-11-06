import sys
sys.stdin = open('input.txt')

'''
'o' : omok exist
'.' : not exist
'''

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
            if five >= success:
                result = 'YES'

    # sero
    for i in range(N):
        five1 = 0
        for j in range(N):
            if omok[j][i] == 'o':
                five1 += 1
            if five1 >= success:
                result = 'YES'

    # deagak
    for i in range(N):
        five2 = 0
        if omok[i][i] == 'o':
            five2 += 1
        if j == N-1 and omok[i][i] == '.':
            if five2 >= success:
                result = 'YES'
            # five2 = 0
    # deagak
    for i in range(N):
        five3 = 0
        if omok[i][N-1-i] == 'o':
            five3 += 1
        if j == N - 1 and omok[i][N-1-i] == '.':
            if five3 >= success:
                result = 'YES'
            # five3 = 0
    print(f'#{tc} {result}')