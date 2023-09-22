import sys
sys.stdin = open('input.txt')

# 격자판의 숫자 이어 붙이기
T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 특정 위치를 기점으로 상하좌우 문자를 붙여야 하므로
# 파라미터로 좌표값도 받아야 한다.
def dfs(y, x, number):
    # 길이가 7이 되면 재귀 종료
    if len(number) == 7:
        result.add(number)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        # 갈 수 없는 위치면 continue
        if ny < 0 or ny >= 4:
            continue

        if nx < 0 or nx >= 4:
            continue

        # 갈수 있다면, 다음 위치로 ㄱㄱ
        dfs(ny, nx, number + maps[ny][nx])


for tc in range(1, T+1):
    maps = [input().split() for _ in range(4)]

    # 7자리 수를 중복 제거하여 저장
    result = set()

    # 시작지점 == 모두 보아야 한다.
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')