# 연속한 1의 개수
import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split('0'))
    # print(arr)
    result = 0
    for i in range(len(arr)):
        if result < len(arr[i]):
            result = len(arr[i])

    print(f'#{tc} {result}')
