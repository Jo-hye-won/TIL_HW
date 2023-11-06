import sys
sys.stdin = open('input.txt')

T = 10
W = 100

for tc in range(1, T+1):
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    while dump_cnt > 0:
        dump_cnt -= 1
        boxes[-1] -= 1
        boxes[0] += 1
        boxes.sort()

    result = max(boxes) - min(boxes)
    print(f'#{tc} {result}')