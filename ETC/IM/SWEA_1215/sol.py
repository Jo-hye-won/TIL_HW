import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    K = int(input())
    N = 8
    arr = [input() for _ in range(N)]
    # print(arr)
    cnt = 0  # 회문개수 세려고
    for i in range(N):
        for j in range(N - K + 1):
            for p in range(K // 2):
                if arr[i][j + p] != arr[i][j + K - 1 - p]: #  가로
                    break  # for p, j부터 시작하는 구간은 회문이 아님
            else:   # for이 끝나고 실행되는 행
                    # 근데 만약 break가 실행된 상태면 이거 실행 안됨
                cnt += 1
            for p in range(K // 2):
                if arr[j + p][i] != arr[j + K - 1 - p][i]: # 세로
                    break  # for p, j부터 시작하는 구간은 회문이 아님
            else:
                cnt += 1
    print(f'#{tc} {cnt}')

#
# K = int(input())
# arr = [input() for _ in range(8)]
# ★ col_words = [''.join(row) for row in zip(*arr)]  ★
# print(arr)
# print(col_words)
# #
# # x = [0,0,0,0,2,4,5]
# # y = [1,2,3,4,5,6]
# # for x,y in zip(x,y):
# #     print(x,y)