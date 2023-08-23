import sys
sys.stdin = open('input.txt')

'''
4 = 0100
7 = 0111
F = 1111
E = 1110
'''

T = int(input())

for tc in range(1, T+1):
    N, N16 = input().split()
    # print(N, N16)
    answer = ''
    for char in N16:
    #     result = bin(int(char, base=16))[2:]
    #     while len(result)!= 4:
    #         result = '0' + result
    #     answer += result
    # print(answer)
        print(bin(int(char, base=16))[2:].zfill(4), end='') # zfill = 크기가 4가될때까지 0으로 채운다
    print(answer)