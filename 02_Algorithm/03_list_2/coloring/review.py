import sys
sys.stdin = open('input.txt')
'''
color = 1(빨강)
color = 2(파랑)
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    tmp = [[0] * 10 for _ in range(10)]  # 색칠할 범위 카운트해서 입력해 둘 배열 만들기
    # print(tmp)
    print(arr)
    for i in arr:  # 배열에서 리스트 하나씩 꺼내와진다.
        for j in range(i[0], i[2] + 1):
            for k in range(i[1], i[3] + 1):
                if i[4] == 1:
                    tmp[j][k] += 1
                # elif i[4] == 2:
                #     tmp[j][k] += 2
                else:
                    tmp[j][k] += 2
    purple = 0
    for x in range(10):
        for y in range(10):
            if tmp[x][y] == 3:
                purple += 1

    print(f'#{tc} {purple}')