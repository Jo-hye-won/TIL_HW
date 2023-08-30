# a = [3,6,7,1,5,4]
# N = 6
#
# for i in range((1, 1<<(N-1)):
#     subset1 = []
#     subset2 = []
#     for j in range():
#         if i & (): # j번 비트가 0이 아니면
#             subset1.append(a[j])
#         else:
#             subset2.append(a[j]) # 0인 애들
#     print(subset1,subset2)


a = [3, 6, 7, 1, 5, 4]
N = 6
b = [1, 2, 3, 4]
M = 4

# for i in range(1, (1 << N) - 1):
for i in range(1, (1 << M) // 2):   # 1 << (N-1) == (1 << N) // 2
    subset1 = []
    subset2 = []
    # total1 = 0
    # tatal2 = 0
    for j in range(M):
        if i & (1 << j):    # j 번 비트가 0이 아니면
            subset1.append(b[j])
        else:
            subset2.append(b[j])
    # r1 = f(subset1)
    # r2 = f(subset2)
    # if r1 and r2:
    #     if min_v > abs(total1 - total2):

    print(subset1, subset2)