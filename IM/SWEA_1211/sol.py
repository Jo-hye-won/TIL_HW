import sys
sys.stdin = open('input.txt')

    # 하, 좌, 우
dx = [1, 0, 0]
dy = [0, -1, 1]

def check(x, y):
    visited = [[0] * 100 for _ in range(100)]
    original = y
    visited[x][y] = 1
    while x != 99:
        for i in range(3):
            ni = x + dx[i]




T = 10
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[0][i] == 1: # 1


