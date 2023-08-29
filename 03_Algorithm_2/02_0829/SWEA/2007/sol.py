import sys
sys.stdin = open('input.txt')

T = int(input())
M = 10
for tc in range(1, T+1):
    test = list(map(str, input()))
    max_l = 0
    for l in range(1, M+1):
        if test[:l] == test[l:l*2]:
            max_l = l
            break
    print(f'#{tc} {l}')
