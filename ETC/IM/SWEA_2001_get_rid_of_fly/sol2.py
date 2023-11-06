import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N = 배열 / M = 파리채크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_2 = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            paris = 0

            for k in range(M):
                for l in range(M):
                    paris += arr[i+k][j+l]

            arr_2.append(paris)

    print(f'#{tc} {max(arr_2)}')