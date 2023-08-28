import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrot = sorted(map(int, input().split()))
    A = N // 2
    min_v = 1000  # 포장별 최소 개수 차이

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if carrot[i] != carrot[i + 1] and carrot[j] != carrot[j + 1]:
                s = i + 1
                m = j - i
                l = N - 1 - j

                if s <= A and m <= A and l <= A:
                    if min_v > (max(s, m, l) - min(s, m, l)):
                        min_v = max(s, m, l) - min(s, m, l)
    if min_v == 1000:
        min_v = -1

    print(f'#{tc} {min_v}')