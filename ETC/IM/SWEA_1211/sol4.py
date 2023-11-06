import sys
sys.stdin = open('input.txt')

    # 하, 좌, 우
dx = [0, 0, 1]
dy = [1, -1, 0]


def check(x, y):
    visited = [[0] * 100 for _ in range(100)]
    original = y
    visited[x][y] = 1
    cnt = 0
    while x != 99:
        for k in range(3):
            ni = x + dx[k]
            nj = y + dy[k]
            if 0 <= ni < N and 0 <= nj < N and ladder[ni][nj] and visited[ni][nj] == 0:
                x, y = ni, nj
                visited[ni][nj] = 1
                cnt += 1
                break
    return [cnt, original]  # 이동거리와,  좌표값을 리스트에 넣어서 반환한다.


T = 10
N = 100
for _ in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]
    cnt_list = []  # check 함수에서 반환되는 리스트 넣을 리스트 만들어두기

    for i in range(N): # N크기의 사다리라서 그 길이만큼 순회하면서
        if ladder[0][i] == 1:  # 첫번째 행의 값이 1이면 시작지점이다
            # 그때의 이동거리와, 좌표값리스트를 구하기 위한 check함수 호출 및 cnt_list에 담기
            cnt_list.append(check(0, i))

    cnt_list.sort()  # 기본정렬은 리스트의 리스트 첫번째 값을 기준으로 오름차순 정렬된다.
    result = cnt_list[0][1] # 정렬해뒀으니까 제일 앞에 있는 것의 이동거리가 제일 작을 것이고
                            # 그때의 x좌표를 result에 할당한다.
    print(f'#{tc} {result}')





