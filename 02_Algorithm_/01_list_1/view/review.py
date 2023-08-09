import sys
sys.stdin = open('view.txt')

T = 10
# result = 0
for tc in range(1, T+1):
    H = int(input())
    building = list(map(int, input().split()))
    view = 0
    for i in range(2, H-2):
        max_view = building[i-2]
        if max_view < building[i - 1]:
            max_view = building[i - 1]
        if max_view < building[i + 1]:
            max_view = building[i + 1]
        if max_view < building[i + 2]:
            max_view = building[i + 2]
        if building[i] > max_view:
            result = building[i] - max_view
            view += result

    print(f'#{tc} {view}')