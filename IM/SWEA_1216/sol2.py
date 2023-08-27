import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    input()
    N = 100
    lst = [list(input()) for _ in range(N)]
    # res = f(lst, N)
    # print(f'#{tc} {res}')
    MAX = 1

    for k in range(N, 0, -1):
        for i in range(N):
            for j in range(N-k+1):
                for p in range(k // 2):
                    check = True
                    if lst[i][j+p] != lst[i][j+k-1-p]:
                        check = False
                        break
                if check:
                    MAX = max(MAX, k)

                for p in range(k // 2):
                    check = True
                    if lst[j+p][i] != lst[j+k-1-p][i]:
                        check = False
                        break
                if check:
                    MAX = max(MAX, k)
    print(f'#{tc} {MAX}')