import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = [n for n in range(1, N+1)]
# print(numbers)
ls = []

for i in numbers:
#     # str(i)
#     ls.append(i)
# # print(ls)
# #
# #
    if i % 3 == 0:
        leng = i//3
        res = '-'*leng
    else:
        res = i
    print(res, end=' ')