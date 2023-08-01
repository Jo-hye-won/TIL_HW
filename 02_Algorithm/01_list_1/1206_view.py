import sys
sys.stdin = open('view.txt')

T = 10                      # TC 10개 고정
for tc in range(1, T+1):    # 10번 돌면서
    N = int(input())        # 가로 길이(N개의 건물)
    height = list(map(int, input().split()))   # 건물 높이 노나서 받아오기

    view = 0    # 초기값 설정
    for i in range(2, N-2):
        # 2 이상의 공간이 확보 되어야하니까 i-2부터 비교하기 위해서 설정
        max_v = height[i-2]
        # max_v = 0
        if max_v < height[i-1]:   # i-1과 비교
            max_v = height[i-1]
        if max_v < height[i+1]:  # i+1과 비교
            max_v = height[i+1]
        if max_v < height[i+2]:  # i+2과 비교
            max_v = height[i+2]
        # if max_v < height[i-2]:  # i-2과 비교
        #     max_v = height[i-2]       # 얘는 제거해도 됨
        if height[i] > max_v:  # i가 주변 보다 높으면
            view += height[i] - max_v

    print(f'#{tc} {view}')



# 방법 2
    T = 10
    for tc in range(1, 11):
        N = int(input())
        height = list(map(int, input().split()))

        view = 0
        for i in range(2, N - 2):
            max_v = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
            if height[i] > max_v:
                view += height[i] - max_v

        print(f'#{tc} {view}')

    # 1 691
    # 2 9092
    # 3 8998
    # 4 9597
    # 5 8757
    # 6 10008
    # 7 10194
    # 8 10188
    # 9 9940
    # 10 8684