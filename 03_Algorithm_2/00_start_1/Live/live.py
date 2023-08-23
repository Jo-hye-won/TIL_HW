'''
1
2 3
1 2 3
4 5 6

'''


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 2차원 배열 0으로 둘러쌓이게 만들기
    arr = [[0]*(M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(M+2)]
    print(arr)
