T = 10                      # TC 10개 고정
for tc in range(1, T+1):    #
    N = int(input())        # 가로 길이
    height = list(map(int,input().split()))


    view = 0
    for i in range(2, N-2):
        max_v = height[i-2]
        if max_v < height[i-1]:
            max_v = height[i-1]
        if max_v < height [i+2]:
            max_v = height[i+2]
        if height[i] > max_v :  # i가 주변 보다 높으면
            view += height[i] - max_v

    print(f'#{tc} view')