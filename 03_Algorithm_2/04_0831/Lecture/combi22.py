
# 중복 있는 조합  i)

# 현재 조사 위치 : now
# r : 최대 조사 대상 수
def comb(now, r, idx):
    if now == r:
        print(check)
    else:
        for i in range(idx, len(num)):
            check[now] = num[i]
            comb(now+1, r, i)


num = [1, 2, 3]
check = [0] * len(num)
comb(0, 3, 0)