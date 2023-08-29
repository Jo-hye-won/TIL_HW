import sys
sys.stdin = open('input.txt')

'''
1부터 N
홀수는 더하고
짝수는 빼기

 
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # numbers = a for a in range(1)