import sys
sys.stdin = open('input.txt')

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
    'F': '1111',
}

T = int(input())

for tc in range(1, T+1):
    N, N16 = input().split()
    result = ''
    for char in N16:
        result += hex_to_bin[char]

    print(N16)
    print(result)
    print(int(result,base=2)) # 다시 10진법으로 바꾸기
