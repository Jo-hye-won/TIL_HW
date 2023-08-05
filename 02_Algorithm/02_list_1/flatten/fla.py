import sys
sys.stdin = open('input.txt')

T = 10      # 테스트 케이스
for tc in range(1, T+1):  # 10번 순회하면서
    N = int(input())      # 덤프 횟수 입력받고
    height = list(map(int, input().split()))    # 각 상자의 높이 리스트에 담고

    answer = 0  # 최고점과 최저점의 차이를 0으로 두고 시작
    while N > 0:  # 덤프횟수가 소진될때까지!
        N -= 1  # 한번 덤프할 때마다 덤프횟수 1 감소
        min_ = 0   # 최소값 초기설정
        max_ = 0   # 최대값 초기설정
        for i in range(1,100):   # 가로길이 100이니까 100까지 순회하면서
            if height[min_] > height[i]:    # 가장 낮은 곳
                min_ = i
            if height[max_] < height[i]:    # 가장 높은 곳
                max_ = i
        if height[max_] - height[min_] < 2:  # 평탄화 완료조건
            answer = height[max_] - height[min_]
            break
        else:
            height[max_] -= 1  # 가장 높은 상자를
            height[min_] += 1  # 가장 낮은 곳으로 이동

    if N == 0:  # 평탄화 다 못했는데 덤프횟수를 모두 채운 경우, 그때의 최고,최저높이 검색
        min_ = 0
        max_ = 0

        for i in range(100):
            if height[min_] > height[i]: # 가장 낮은 곳
                    min_ = i
            if height[max_] < height[i]: # 가장 높은 곳
                    max_ = i
        answer = height[max_] - height[min_]
    print(f'#{tc} {answer}')




