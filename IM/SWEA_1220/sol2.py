import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for j in range(n):

        stack = []
        r, c = 0, j

        while r < n:
            if not stack and li[r][c] == 1:
                stack.append(1)

            elif stack and li[r][c] == 2:
                stack.pop()
                cnt += 1
            r += 1

    print(f'#{tc} {cnt}')