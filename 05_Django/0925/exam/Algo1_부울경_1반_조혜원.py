import sys
sys.stdin = open('algo1_sample_in.txt')

hex_to_dec = {hex(val)[2:].upper():val for val in range(16)}

T = int(input())
for tc in range(1, T+1):
    N = input()
    data = input()
    key = input()
    result = ''
    for char in data:
        result += hex_to_dec[char] ^ hex_to_dec[key][2:].upper()
    print(f'#{result}')

