def f(i, N):
    if i == N:
        print(bit)
        for j in range(N):
            if bit[j]:  # 비트j 가 1이면
                print(A[j], end = ' ')  # A의 j번 요소가 포함되어 있어
        print()
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
