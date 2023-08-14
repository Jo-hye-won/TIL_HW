
''' NxN 배열형태의 지도 
인접 = 상하좌우 
지도의 가장자리는 인접한 지역이 3곳 또는 2곳일 수 있음

주변의 높이보다 높으면 봉우리가 된다
봉우리에 해당하는 모든 지역을 찾아보자

'''
# 지도의 개수
T = int(input()) # => 3개

    # 상  우  하  좌 비교할 위치 좌표로 옮겨가기 위한 설정
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):  # T만큼 반복하면서
    N = int(input())   # 지도의 가로세로 크기 = N
    # N개의 줄에 걸쳐서 N개의 높이 h 주어짐  # h들이 모여있는 리스트 배열 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]
    b_cnt = 0  # 봉우리 개수(봉우리에 해당하는 지역의 수) 세기위한 값 초기화
    # cnt = 0
    for i in range(N):
        for j in range(N):
            point_h = arr[i][j]
            cnt = 0
            # 상하좌우높이와 비교해서 가운데높이가 상하좌우보다 '다' 높으면 봉우리 개수 + 1
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    compare_h = arr[ni][nj]  # 비교할 높이
                    if compare_h < point_h:  # print(compare_h)
                            b_cnt += 1
                        # for l in range(N):
                        #     if ni ==
                        if ni == 0 and nj == 0 and cnt == 2:
                            b_cnt += 1
                        if ni == 1 and nj == 0:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 2 and nj == 0:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 4 and nj == 0:
                            if cnt == 2:
                                b_cnt += 1

                        if ni == 0 and nj == 1:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 0 and nj == 2:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 0 and nj == 3:
                            if cnt == 2:
                                b_cnt += 1

                        if ni == 1 and nj == 3:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 2 and nj == 3:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 3 and nj == 3:
                            if cnt == 2:
                                b_cnt += 1

                        if ni == 3 and nj == 1:
                            if cnt == 3:
                                b_cnt += 1
                        if ni == 3 and nj == 2:
                            if cnt == 3:
                                b_cnt += 1

    if b_cnt > 0:
        print(f'#{tc} {b_cnt}')
    else:       # 봉우리가 없는 경우는 0을 출력
        print(f'#{tc} 0')
    #

'''    print(arr)
       0  1  2  3
   0 [[1, 1, 2, 1], 
   1 [2, 1, 3, 1], 
   2 [2, 1, 2, 1], 
   3 [3, 4, 4, 4]]
    [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    [[2, 3, 2, 1, 3], [2, 2, 1, 3, 2], [2, 2, 2, 3, 2], [1, 3, 3, 3, 1], [1, 4, 2, 2, 2]]
    
'''
#                    break
#             else:
#                 cnt +=1
# print(f'#{tc} {cnt}')