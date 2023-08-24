import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    table_10 = [[0]*10 for _ in range(10)] # 리스트 콤프리핸션

    for i in arr:
        for j in range(i[0], i[2] + 1):
            for k in range(i[1], i[3] + 1):
                if i[4] == 1:
                    table_10[j][k] += 1
                else:
                    table_10[j][k] += 2

    count_color = 0
    for i in range(10):
        for j in range(10):
            if table_10[i][j] == 3:
                count_color += 1

    print(f'#{tc} {count_color}')




