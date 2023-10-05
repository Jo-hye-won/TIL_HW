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

    # =====================================================================

    import sys

    sys.stdin = open('input.txt')

    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
        '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
        'F': '1111',
    }

    T = int(input())

    for tc in range(1, T + 1):
        N, N16 = input().split()
        result = ''
        for char in N16:
            result += hex_to_bin[char]

        print(N16)
        print(result)
        print(int(result, base=2))  # 다시 10진법으로 바꾸기

    #=======================================================================
    import sys

    sys.stdin = open('input.txt')

    # hex_to_bin = {hex(i).replace('0x','').upper() : f'{i:04b}' for i in range(16)}
    # print(hex_to_bin)
    T = int(input())
    hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                  '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                  'E': '1110', 'F': '1111'}
    for tc in range(1, T + 1):
        N, N16 = input().split()