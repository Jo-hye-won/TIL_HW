# 정식이의 은행업무

import sys
sys.stdin = open('input.txt')

import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    A = input()         # 2진수
    B = list(map(int, input()))   # 3진수

    N = len(A)      # N 자릿수 2진수
    M = len(B)      # M 자릿수 3진수
    ans = 0

    binary = int(A, 2)  # 정수로 변환
    bin_list = [0] * N  # 각 비트를 반전시킨 수 N개 저장
    # 각 비트를 반전시킨 2진수 만들기...
    for i in range(N):
        bin_list[i] = binary ^ (1 << i)  # ^ => or  # i번째 수를 반전

    for j in range(M):  # 3진수의 B[i]자리를 바꾼 숫자 만들기
        num1 = 0    # (B[i] + 1) % 3
        num2 = 0    # (B[i] + 2) % 3
        for k in range(M):
            if j != k:
                num1 = num1 * 3 + B[k]
                num2 = num2 * 3 + B[k]
            else:
                num1 = num1 * 3 + (B[k]+1) % 3
                num2 = num2 * 3 + (B[k]+2) % 3
        if num1 in bin_list:
            ans = num1
            break   # for i
        if num2 in bin_list:
            ans = num2
            break   # for i

    print(f'#{tc} {ans}')