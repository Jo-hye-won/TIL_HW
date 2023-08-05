import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    # print(boxes)
    result = 0
    # for box in boxes:
    #     # print(box)
    for i in range(N):
        max_box = N - (i + 1)
        for j in range(i+1, N):
            if boxes[i] <= boxes[j]:
                max_box -= 1
        if result < max_box:
             result = max_box

    print(f'#{tc} {result}')