import sys
sys.stdin = open('input.txt')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    idx = 0 # 상하좌우 순으로 조사
    cnt = 1
    while idx < 4: # 4방향을 모두 조사하면 종료
        nx = x + dx[idx]
        ny = y + dy[idx]
        # 새 좌표  nx, ny로 이동 가능한지 판별
        if 0 <= nx < N and 0 <= ny < N and arr[x][y] + 1 == arr[nx][ny]:
            x, y = nx, ny # 이동 가능하면, 내 현재 좌표를 바꿔치기
            cnt += 1 # 이동했으니 이동한 횟수 +1
            idx = 0 # 이동한 좌표에서 다시 처음부터 조사하도록 idx 초기화
        # 다음 방향 조사
        idx += 1 # 통과 못했으면 다음 위치 조사해야지
    return cnt



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    result = [] # 답안 기록용(모든 좌표에 대한, 방 번호와 이동횟수 기록)

    # 모든 좌표에 대해서 delta탐색
    for i in range(N):
        for j in range(N):
            # 각 좌표 i, j에 대해서
            # 방 번호, 누적한 이동 횟수
            # 모두 기록하고 난 다음에, 그 중에, 이동 가장 많이 한 경우
            # 조사를 통해 얻고자 하는 값은? i,j 좌표에서 출발했을 때의 이동 횟수
            result.append((search(i, j),arr[i][j]))
    result.sort(key=lambda x: (x[0], -x[1]))
    print(result[-1][1], result[-1][0])