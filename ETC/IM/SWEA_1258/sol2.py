import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0:  # 0이 아닐때 좌표
                y, x = i, j

                while y < N and MAP[y][j] != 0:  # y가 N 크기 보다 작고
                    y += 1  # MAP[y][j] 값이 0이 아닐떄 y 1씩 증가

                while x < N and MAP[i][x] != 0:
                    x += 1

                if MAP[i][j] != 0:  # MAP[i][j]가 0이 아닐 때
                    lst.append((y - i, x - j))  # lst에 튜플형식으로 좌표 저장
                    print(lst)
                for k in range(i, y):  # i에서 y까지(y포함X)
                    for l in range(j, x):  # j에서 x까지 (x포함X)
                        MAP[k][l] = 0  # 지나온곳 0으로 바꿔줌 그러면 최대값만 남음
    # lst sort할때 key값 이용 정렬 lambda 함수에서 a는 lst요소값
    # 그래서 a[0]* a[1] 곱한 값과 같을땐 a[0]순으로 정렬
    lst.sort(key=lambda a: (a[0] * a[1], a[0]))

    print(f'#{tc} {len(lst)}', end=' ')
    for y, x in lst:
        print(f'{y} {x}', end=' ')
    print()