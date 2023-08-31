

# 중복 없는 조합 i+1)

# 현재 조사 위치 : now
# r : 최대 조사 대상 수
def comb(now, r, idx):
    if now == r:
        print(check[:r]) # r개까지만 보여줘
    else:
        for i in range(idx, len(num)):
            check[now] = num[i]
            comb(now+1, r, i+1)


num = [1, 2, 3]
check = [0] * len(num)
comb(0, 2, 0)