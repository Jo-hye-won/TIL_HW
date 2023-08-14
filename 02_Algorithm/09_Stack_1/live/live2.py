def fibo(n):
    global cnt   # 해야 됨
    global memo  # 안해도 됨
    cnt += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

N = 30
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
cnt = 0
print(fibo(N), cnt)
