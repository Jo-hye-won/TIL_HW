import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    # print(N,K)
    # print(scores)
    scores.sort()
    sum_ls = []
    for i in range(K):
        sum_ls.append(scores.pop())

    result = 0
    for j in range(len(sum_ls)):
        result += sum_ls.pop()

    print(f'#{tc} {result}')