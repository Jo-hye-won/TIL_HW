import sys
sys.stdin = open('view.txt')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 건물의 개수
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-1):
        point = buildings[i]
        for j in range(i-2, i+3):
            if i == j:
                continue
            if buildings[i] > buildings[j] and point > buildings[i] - buildings[j]:
                point = buildings[i] - buildings[j]
                print(point,'point')
                print(buildings[i])
            if buildings[i] <= buildings[j]:
                break

        else:
            cnt += point
    # print(cnt)