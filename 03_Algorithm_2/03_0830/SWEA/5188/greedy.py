import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 완전 검색
    for i in range(N):
        for j in range(N):
            # 첫 시작지점 0, 0
            if i == j == 0:
                continue
            # 다음칸 이동하면서 누적값 계산
            # i == 0
            if i == 0:
                # 첫번째 행이라면, 최적의 해를 구할 방법이
                # 내 위치의 왼쪽에서 온 값밖에 없다.
                arr[i][j] += arr[i][j-1]
            elif j == 0:
                arr[i][j] += arr[i-1][j] # 위에서 온 값
            # 위 두가지 경우를 제외한 모든 경우에 대해서는
            # 항상, 위쪽과 왼쪽으로부터 넘어온 누적값중에
            # 제일 작은 값을 내 위치에 누적하면
            # 그게 최적해
            else:
                arr[i][j] += min(arr[i-1][j], arr[i][j-1])
    # print(arr)
    print(f'#{tc} {arr[N-1][N-1]}')