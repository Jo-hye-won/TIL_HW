import sys
sys.stdin = open('input.txt')

# 딕셔너리 이용
binary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
          '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())

for tc in range(1, T+1):
    result = ''
    N, case = input().split()
    for c in case:
        result += binary[c]
    print(f'#{tc} {result}')


# 함수 이용
bin()
hex()
oct()

# base 이용하기
N, B = input().split()
result = int(N, base=int(B))
print(result)

# enumerate 이용하기
# (10진법으로 변환하려면 각 자리의 숫자에 진법의 거듭제곱을 곱해주고
# 이를 모두 더해주면 된다
N, B = input().split()
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = N[::-1]
result = 0

for i, n in enumerate(N):
    result += (int(B)**i)*(arr.index(n))
print(result)