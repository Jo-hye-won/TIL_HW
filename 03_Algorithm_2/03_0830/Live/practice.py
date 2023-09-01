# ```python
# # 반복을 이용한 선택정렬
# def SelectionSort(A):
#     n = len(A)
#     for i in range(0, n-1):
#         minI = i
#         for j in range(i+1, n):
#             if A[j] < A[minI]:
#                 minI = j
#         A[minI], A[i] = A[i], A[minI]
# ```
'''
선택정렬함수(SelectionSort)를 재귀적 알고리즘으로 작성해 보시오.

f(0, N, arr)

f(i, N, arr)
    if i == N-1
    # else: ~
    pass
        # 최소값을 arr[i]에 옮겨놓기
        # f(i+1, N, arr)
'''
T = int(input())


def babygin(counts, index):
    if counts[index] == 3:
        return 1
    # print(index, index-1, index-2)
    for i in (index, index-1, index-2):
        if 0 <= i <= 7 and counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            return 1
    return 0


for t in range(1, T+1):
    lst = list(map(int,input().split()))
    countP1 = [0] * 10
    countP2 = [0] * 10

    result = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            # print(lst[i])
            countP1[lst[i]] += 1
            if babygin(countP1,lst[i]):
                result = 1
                break
        else:
            # print(lst[i])
            countP2[lst[i]] += 1
            if babygin(countP2,lst[i]):
                result = 2
                break

    print(f'#{t} {result}')