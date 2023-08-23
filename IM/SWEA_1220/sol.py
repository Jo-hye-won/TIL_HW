import sys
sys.stdin = open('input.txt')

'''
1 = N극 성질을 가지는 자성체
2 = S극 성질을 가지는 자성체
테이블의 위쪽에 N극
테이블의 아래쪽에 S극
테이블의 앞뒤쪽에 있는 N극 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.
'''

T = 100

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        status = 0
        for j in range(N):
            if table[i][j] == 1:
                status = 1


