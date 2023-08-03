
# # 1
# def print_subset(bit, arr, n):
#     for i in range(n):
#         if bit[i]:
#             print(arr[i], end =' ')  # 부분집합의 합을 구하려면 이부분을 더하기로
#     print(bit)
#
#
# arr = [1,2,3,4]
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i  # bit 첫번째 자리에 0또는 1
#     for j in range(2):
#         bit[1] = j  # bit 두번째 자리에 0또는 1
#         for k in range(2):
#             bit[2] = k  # bit 세번째 자리에 0또는 1
#             for l in range(2):
#                 bit[3] = l      # bit 네번째 자리에 0또는 1
#                 print_subset(bit, arr, 4)


# # 2
# def print_subset(bit, arr, n):
#     total = 0   # 부분집합의 합
#     for i in range(n):
#         if bit[i]:
#             print(arr[i], end =' ')  # 부분집합의 합을 구하려면 이부분을 더하기로
#             total += arr[i]
#     print(bit, total)
#
#
# arr = [1,2,3,4]
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i  # bit 첫번째 자리에 0또는 1
#     for j in range(2):
#         bit[1] = j  # bit 두번째 자리에 0또는 1
#         for k in range(2):
#             bit[2] = k  # bit 세번째 자리에 0또는 1
#             for l in range(2):
#                 bit[3] = l      # bit 네번째 자리에 0또는 1
#                 print_subset(bit, arr, 4)
#
#
# # 3
# arr = [1,2,3]
#
# n = len(arr)        # n : 원소의 개수
# for i in range(1<<n):       # 1 << n: 부분집합의 개수
#     for j in range(n):      # 원소의 수만큼 비트를 비교함
#         if i & (1 <<j):     # i의 j번 비트가 1인 경우
#             print(arr[j], end=', ')     # j번 원소 출력
#     print()
# print()



