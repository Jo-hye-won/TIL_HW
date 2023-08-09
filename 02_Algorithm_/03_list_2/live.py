di = [0,1,0,-1]
dj = [1,0,-1,0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]  # input으로 리스트 만들기

max_v = 0   # 모든 원소가 0 이상이라고 전제깔고 합니다.
for i in range(N):  # 모든 원소 arr[i][j]에 대해..
    for j in range(N):
        # arr[i][j]중심으로
        s = arr[i][j]

        # for k in range(4):
        #     ni, nj = i + di[k], j + dj[k]   # ni와 nj
        #     if 0 <= ni < N and 0 <= nj < N:     # 배열을 벗어나지 않으면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 요롷게도 가능하다
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
        # 여기까지가 주변 원소를 포함한 합

        if max_v < s:  # s > max_v 로 하지말고 헷갈리니까
            max_v = s
print(max_v)

#
# N = int(input())
# arr = [list(map(int, input().split()))] for _ in range(N)]
# total1 = 0
# total2 = 0
# for i in range(N):
#     total1 += arr[i][i]
#     total2 += arr[i][N-1-i]





# N = 2 # 행의 크기
# M = 4 # 열의 크기
#
# arr = [[0,1,2,3],[4,5,6,7]]
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])
'''
0
1
2
3
4
5
6
7
'''
# for j in range(M):
#     for i in range(N):
#         print(arr[i][j])
'''
0
4
1
5
2
6
3
7
'''
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j+(M-1-2*j) * (i % 2)])
'''
0
1
2
3
7
6
5
4
'''
# for i in range(N):
#     for j in range(M):
#         if i % 2 : # 홀수번 행인 경우
#
#         else:


#
# N = 2 # 행의 크기
# M = 4 # 열의 크기

# arr = [[0,1],[4,5,6,7]]
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])
# => error

# arr = [[0,1],[4,5,6,7]]
# for i in range(N):
#     for j in range(len(arr[i])):
#         print(arr[i][j])
'''
0
1
4
5
6
7
'''

# N = 2
# M = 4
# arr = [[0] * M for _ in range(N)]
# arr2 = [[0] * M] * N   # => 이케 하면 앙대!! ★
# print(arr)      # [[0, 0, 0, 0], [0, 0, 0, 0]]
# print(arr2)     # [[0, 0, 0, 0], [0, 0, 0, 0]]
# arr[0][0] = 1
# arr2[0][0] = 1
# print(arr)      # [[1, 0, 0, 0], [0, 0, 0, 0]]
# print(arr2)     # [[1, 0, 0, 0], [1, 0, 0, 0]]


# N = 2
# M = 4
# arr = [[0,1,2,3],[4,5,6,7]]
#
# max_v = 0
# for i in range(N):
#     row_total = 0       # 각 행의 합
#     for j in range(M):
#         row_total += arr[i][j]
#     if max_v < row_total:
#         max_v = row_total
# print(max_v)

'''
3
1 2 3
4 5 6
7 8 9
'''
