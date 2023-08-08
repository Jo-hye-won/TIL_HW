T = int(input())

for tc in range(1, T+1):
    A = tuple(set(input()))
    B = input()
    num_li = [0] * len(A)
    for i in A:
        for j in range(len(B)):
            if i == B[j]:
                num_li[A.index(i)] += 1

    MAX = 0
    for i in range(len(num_li)):
        if MAX < num_li[i]:
            MAX = num_li[i]

    print(f'#{tc} {MAX}')