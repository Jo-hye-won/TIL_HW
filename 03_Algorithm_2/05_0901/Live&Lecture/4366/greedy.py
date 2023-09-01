# 정식이의 은행업무

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    T2 = list(map(int, input()))   # 2진수
    T3 = list(map(int, input()))   # 3진수
    print(T2, T3)
    # 2진수 전체순회
    for i in range(len(T2)):
        tmp2 = list(T2)
        tmp2[i] = tmp2[i] ^ 1
        # print(tmp2)

    # tmp2에 들어간 간 각 경우의 수와 비교할 3진수
        for j in range(len(T3)):
            tmp3 = list(T3)
            # 3진수의 경우의 수 : 0, 1, 2
            for k in range(3):
                if tmp3[j] != k:
                    tmp3[j] = k

                a = ''.join(map(str, tmp2))
                b = ''.join(map(str, tmp3))
                # print(a, b)

                if int(a, 2) == int(b, 3):
                    print(f'#{tc} {int(a, 2)}')