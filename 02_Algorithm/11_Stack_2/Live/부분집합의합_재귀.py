
def f(i, N, s):  # s: i-1원소까지의 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end=' ')  # 경우의 수
        print(f' : {s}')
        return
    else:
        bit[i] = 1  # 부분집합에 A[i]가 포함
        f(i+1, N, s+A[i])  # 포함되니까 더해서 넘겨줌
        bit[i] = 0  # 부분집합에 A[i]가 빠짐(미포함)
        f(i+1, N, s)  # A가 추가 되지 않았으니까 합이 앞과 똑같아
        return

A = [1, 2, 3]
bit = [0] * 3
f(0, 3, 0)
