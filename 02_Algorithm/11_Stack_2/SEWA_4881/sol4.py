def f(i, total):
    global ans
    if i == N: # i 가 N 값일때,
        if ans > total:  # ans변수에 total값 넣으며 함수 끝
            ans = total
            return
        # print(MAP)

    if total > ans: # total 값이 ans보다 크면 실행종료
        return      # 가지치기

    for j in range(N):
        if j not in visited:
            visited.append(j)
            f(i+1, total+MAP[i][j])
            visited.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    ans = 300000
    visited = []
    f(0, 0)

    print(f'#{tc} {ans}')
