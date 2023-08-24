import sys
sys.stdin = open('input.txt')
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for _ in range(1, T+1):
    tc, N = map(str, input().split())
    arr = list(map(str, input().split()))


