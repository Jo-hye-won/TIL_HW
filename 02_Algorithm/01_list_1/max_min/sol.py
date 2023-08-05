import sys
sys.stdin = open('input.txt')

T = int(input())

def max_min(ls):
    result = ls[-1] - ls[0]
    return result

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j+1], arr[j]
    # 방법 1
    # result = arr[-1] - arr[0]
    # print(f'#{tc} {result}')
    # print(arr)

    # 방법2
    # result = max_min(arr)
    # print(f'#{tc} {result}')

    # 방법3
    print(f'#{tc}',max_min(arr))
#
# list = [2,3,5,7,9,6]
# N=6
# for i in range(N-1,1,-1):
#     for j in range(i):
#         if list[j] > list[j+1]:
#             list[j],  list[j+1] =  list[j+1],  list[j]
# print(list)

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))    # 각각을 정수형으로 변환해서 리스트로 저장
#     max_val = arr[0]    # 제일 앞에 있는 값으로 초기화
#     min_val = arr[0]    # 1000000(가장 큰값)으로 초기화해도 된다
#     for i in range(1, N):
#         if max_val < arr[i]:
#             max_val = arr[i]
#         if min_val > arr[i]:
#             min_val = arr[i]
#     ans = max_val - min_val
#     print(f'#{tc} {ans}')