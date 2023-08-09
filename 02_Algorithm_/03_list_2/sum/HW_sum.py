import sys
sys.stdin = open('input.txt')

T = 10  # 테스트 케이스 10개
N = 100     # 행,열 100 X 100


for tc in range(1, T+1):       # 테스트 케이스 10번 돌면서
    a = int(input())    # 젤위에 있는거 하나 이상한 입력 없애주고
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열만들어주기
    max_idx = 0  # 최종 가장 큰 값 구하기 위한 초기설정

    # hang_sum = 0  # 여기서 선언하면 안돼!! 그럼 i도 다 순회하고 나서야 초기회됨
    for i in range(N):  # 행을 100번 돌면서 합을 구합시다
        hang_sum = 0    # 행의 합을 구하기 위한 초기값 설정
                        # 한 행을 조회할때마다 초기화 되기 위해서 여기 있어야 함
                        # 변수 선언시점이 굉장히 중요함!!!★★
        for j in range(N):
            plus = arr[i][j]   # i가 0일때 j 0-100 돌고 / i가 1일때 j 0-100돌고 쭉쭉쭉 i= 100,  j=100까지
            hang_sum += plus    # hang_sum에 누적해서 더해주기
        if hang_sum > max_idx:      # 최종가장 큰값이랑 비교해서 큰 값을 max_idx에 저장
            max_idx = hang_sum
        # print(hang_sum)

    # yul_sum = 0
    for i in range(N):
        yul_sum = 0
        for j in range(N):
            plus = arr[j][i]
            yul_sum += plus
        if yul_sum > max_idx:   # 최종가장 큰값이랑 비교해서 큰 값을 max_idx에 저장
            max_idx = yul_sum
        # print(yul_sum)

    # degak_sum = 0
    for i in range(N):      # 대각선은 행,열값 같아야 하니까 i만 돌리면서
        degak_sum = 0
        # for j in range(N):    # j를 돌려버리면 arr[i][i]값이 100번 누적되버림 이상한값 나오게됨
        plus = arr[i][i]        # 대각선은 행,열값 같아야 하니까 i만 돌리면서
        degak_sum += plus
    if degak_sum > max_idx:   # 최종가장 큰값이랑 비교해서 큰 값을 max_idx에 저장
        max_idx = degak_sum
        # print(degak_sum)

    # degak2_sum = 0
    for i in range(N):
        degak2_sum = 0
        # for j in range(N):
        plus = arr[i][100-1-i]     # 100-1-i은 len(arr) -1 -j이다. 대각선을 거꾸로 해야해서!
        degak2_sum += plus
    if degak2_sum > max_idx:   # 최종가장 큰값이랑 비교해서 큰 값을 max_idx에 저장
        max_idx = degak2_sum
        # print(degak2_sum)


    print(f'#{tc} {max_idx}')

# dj = []
# for j in range(1, N+1):
#     dj.append(j)
#
# for i in range(N):
#     for j in range(N):
#         s = arr[0][0]
#         for re in range(99):
#             ni = 0
#             nj = 0 + dj[re]



# print(f'#{tc} {}')