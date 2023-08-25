import sys
sys.stdin = open('input.txt')

T = int(input())
N = 100

for _ in range(1, T+1):
    tc = int(input())
    pallin = [input() for _ in range(N)]
    print(pallin)