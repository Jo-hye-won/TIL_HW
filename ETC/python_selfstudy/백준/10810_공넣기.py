# 바구니 N개
N, M = map(int, input().split())

tmp = [0] * N   # 바구니개수만큼 배열 만들어두기

for l in range(M):  # 공 M번 넣을거야
    i, j, k = map(int, input().split())
    ls = [k] * (j-i+1)
    tmp[i-1: j] = ls  # 바꿔넣어줄 리스트의 길이는
                    # 들어갈 인덱스의 길이와 같아야 한다.

print(*tmp)
# print(tmp)  # [1, 2, 1, 1, 0]