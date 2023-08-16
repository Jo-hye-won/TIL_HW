def f(i, N):
    if i == N:
        print(bit, end = ' ')  # 경우의 수
        s = 0
        for j in range(N):
            if bit[j]:  # 비트j 가 1이면
                s += A[j]
                print(A[j], end = ' ')  # A의 j번 요소가 포함되어 있어
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return

A = [1, 2, 3]
bit = [0] * 3
f(0, 3)
