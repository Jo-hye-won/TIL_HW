T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    N = int(input())  # 행렬크기
    green = list(map(int, input().split()))     # 색칠 할 구간범위 좌표
    '''
    # print(green)
    [1, 1, 3, 4]
    [0, 0, 4, 4]
    [0, 0, 0, 2]
    '''
    arr = [list(map(int, input().split())) for _ in range(N)]  # 평지배열
    # print(arr)

    # 1. 평탄화를 하기 위한 평균값 구하기 먼저 하자!
    h_sum = 0  # 평탄화 영역의 높이 값의 합을 구하기 위한 초기화
    for i in range(green[0], green[2]+1):  # 행우선 순회 1부터 3까지 돌면서
        for j in range(green[1], green[3]+1):  # 열 1부터 4까지
            h_sum += arr[i][j]  # 평탄화 영역의 높이 값의 합 구함

    '''
    # print(h_sum)
    34
    77
    3 
    '''

    # 영역의 칸수
    cnt = (green[2]-green[0]+1) * (green[3]-green[1]+1)

    ''' 
    print(cnt)
    12
    25
    3
    '''
    # 평균값 구해졌다!! 이제 이걸 기준으로 평탄화 작업을 하자
    avg = h_sum // cnt
    # print(type(avg))
    ''' 
    print(avg)
    2
    3
    1
    '''
    # 2. 평탄화
    # def flatten()
    total = 0  # 평탄화 작업 횟수 초기화
    H = avg
    for k in range(green[0], green[2] + 1):  # 행우선 순회 1부터 3까지 돌면서
        for l in range(green[1], green[3] + 1):  # 열 1부터 4까지
            # print(arr[k][l])
            if arr[k][l] > H:   # 기준보다 값이 크면
                total += arr[k][l] - H  # total 값에 값에서 기준을 뺀 값을 더해주고
            elif arr[k][l] < H:     # 기준보다 값이 작으면
                total += H-arr[k][l]    # total에 기준값에서 값을 뺀 값을 더해준다

    print(f'#{tc} {total}')



            # if arr[k][l] == H:     # 기준과 같다면
            #     continue           # 그대로 두고 그냥 넘어가고
            # if arr[k][l] > H:    # 기준인 평균보다 값이 크면
            #     arr[k][l] -= 1     # 값을 1 빼주고
            #     total += 1         # 횟수 1 추가해주기
            # if arr[k][l] < H:   # 기준인 평균보다 값이 작으면
            #     arr[k][l] += 1   # 값을 1 더해주고
            #     total += 1       # 횟수 1 추가해주기

    # #         while green[k][l] == H:
    # #             green[k][l] -= 1  # 값을 1 빼주고
    # #             total += 1