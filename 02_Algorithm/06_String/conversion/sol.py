# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x) - ord('0')
#     return i
#
# print(atoi())
import sys
sys.stdin = open('input.txt')

def itoa(a):
    s = ''
    if a < 0:
        a = -a
    while a > 0:
        ord('0') + a % 10  # 일의 자리 숫자의 ASCII 값
        s += chr(ord('0') + a % 10)  # 일의 자리 숫자의 ASCII 값을
                                     # 빈문자열에다 붙여봐
        a //= 10
        # 음수일 경우에는?
        # if a < 0:
        #     pass
    return s[::-1]

for i in range(1, 7):
    N = int(input())
    result = itoa(N)
    types = type(result)
    print(f'#{i} {result} {types}')


