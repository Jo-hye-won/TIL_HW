import sys
sys.stdin = open('algo1_sample_in.txt')

hex_to_dec = {hex(val)[2:].upper():val for val in range(16)}
print(hex_to_dec)
T = int(input())
for tc in range(1, T+1):
    N = input()
    data = input()
    key = input()
    result = ''
    for char in data:
        result += hex_to_dec[char] ^ hex_to_dec[key][2:].upper()
    print(result)


#  ==========================윤희================================
# 16진수 -> 10진수
hexa_to_ten = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}
# 10진수 -> 16진수
ten_to_hexa = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
               6: '6', 7: '7', 8: '8', 9: '9', 10:'A', 11: 'B',
               12: 'C', 13: 'D', 14: 'E', 15: 'F'}
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    p = input()

    # 16진수 -> 10진수로 바꿔 리스트에 저장
    trans_p = []
    for char in p:
        trans_p.append(hexa_to_ten[char])

    # key도 마찬가지로 변환해준다
    key = input()
    key = hexa_to_ten[key]

    # h를 구할 것이므로
    # 10진수로 변환한 16진수끼리 다시 ^ 연산한다 (pi ^ h)
    # 그 뒤, 계산한 값을 다시 16진수로 변환하여 h에 저장
    h = ''
    for i in trans_p:
        h += ten_to_hexa[i ^ key]

    print(f'#{tc} {h}')


#  ==========================성주================================
import sys
sys.stdin = open('algo1_sample_in.txt')
# Pi = Hi ^ key
# ^은 XOR 둘 다 다르면 1, 같으면 0

dict_16 = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

T = int(input())
for t in range(1, T+1):
    N = int(input())    # N 자리
    P = input()         # 암호화된 N자리 16진수
    key = input()       # 한 자리 16진수

    if key.isdigit():
        key = int(key)
    else:
        key = dict_16[key]

    print(f'#{t}', end= ' ')

    for i in P:
        a = 0
        if i.isdigit():
            a = int(i)^key
        else:
            a = dict_16[i]^key

        if len(str(a)) > 1:
            for k, v in dict_16.items():
                if v == a:
                    print(k, end='')
        else:
            print(a, end='')
    print()