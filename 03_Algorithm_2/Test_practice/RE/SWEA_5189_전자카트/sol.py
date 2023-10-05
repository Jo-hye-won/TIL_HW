import sys
sys.stdin = open('input.txt')






T = int(input())

for _ in range(T):
    N = int(input())
    path = [list(map(int, input().split())) for _ in range(N)]
    # print(path)
    visited = [0] * (N+1)

