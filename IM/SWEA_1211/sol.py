import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

