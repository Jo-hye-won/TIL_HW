
def f(i, N, s, t):  # s: i-1원소까지의 부분집합의 합(포함된 원소의 합)
                    # t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t:      # 현재까지의 합이 너가 원하는 목표치에 도달 했으면
                    # 그만
        print(bit)
        return
    elif i == N:    # 남은 원소가 없는 경우
        return
    elif s > t:     # 남은 원소를 고려할 필요가 없는 경우
        return
    # elif s + 남은 구간의 합 < t:
    #     return
    else:
        bit[i] = 1  # 부분집합에 A[i]가 포함
        f(i+1, N, s+A[i], t)  # 포함되니까 더해서 넘겨줌
        bit[i] = 0  # 부분집합에 A[i]가 빠짐(미포함)
        f(i+1, N, s, t)  # A가 추가 되지 않았으니까 합이 앞과 똑같아
        return


# 1부터 10까지 원소인 집합에서 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print(cnt)
