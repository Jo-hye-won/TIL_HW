# 연속한 1의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))    # 0011001110  # [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    # arr = list(input())              # 글자로 받으려면
    print(arr)

