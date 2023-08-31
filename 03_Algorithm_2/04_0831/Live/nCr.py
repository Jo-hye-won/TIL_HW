# n개에서 r개를 고르는 조합(재귀)
def nCr(n, r, s): # s = 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)



A = [1,2,3,4,5,6]
N = len(A)
R = 2
comb = [0] * R
nCr(N, R, 0)