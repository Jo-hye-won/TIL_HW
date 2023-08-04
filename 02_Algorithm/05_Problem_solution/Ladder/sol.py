import sys
sys.stdin = open('input.txt')

# 하나, 아래로 조사 진행할 것
# 둘, 단, 좌, 우 중 갈 수있는 곳 마주하면 그쪽으로 먼저 갈 것
# 셋, 이미 지나온 길은 다시 돌아가지 않도록 해야함
# 넷, 마지막 행 (99,n)이 되었을 때는 종료되어야 함
# 다섯, 마지막 행에서 마주한 값이 2인 경우, 출발 좌표 출력해야함
# 여섯, 위 모든 과정을 모든 출발점에 대해서 실행해야 함.(반복문 안에서 코드작성해야겠네)
# 이러한 함수를 먼저 만들래

# 이동 하, 좌, 우
dx = [1, 0, 0]
dy = [0, -1, 1]
# 필요인자 : 시작 좌표(x,y)
def search(x,y):
    # 각 시작 좌표들 마다 방문 표시를 위한 2차원 리스트 만들기 ★★★★
    visited = [[0]*100 for _ in range(100)]

    # 만약 2를 찾았을 때, 반환해야 할 시작 좌표 y를 기록
    original_y = y

    # 방문표시
    visited[x][y] = 1

    # 조사 조건은 x가 99가 되기 전까지
    while x != 99:
        # 계속 아래로 조사하면서 진행할거당
        # 조사 순서는? 하, 좌 우?/  하, 우 좌?
        for k in range(3):
            # 다음 조사 위치 좌표
            # 다음 지역 x, y 좌표 | 현재 위치 x,y좌표 + 다음 방향에 대한 좌표
            nx = x + dx[k]
            ny = y + dy[k]

            # 다음 조사를 할 에정지인 (nx,ny) 위치가 안전하게 조사 가능한지
            # 조건으로 확인
            # 다음 조사 가능여부 조건에 data[nx][ny] == 1로 잡으면 발생하는 문제?
            # 2이면 조사를 안해버림 그래서 다음과 같이 3가지 방법이 있음
            # if 0 <= nx < 100 and 0 <= ny < 100 and (data[nx][ny] == 1 or data[nx][ny] == 2):
            # if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] != 1
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] and visited[nx][ny] == 0:
                x, y = nx, ny
                # 이전에 있던 위치를 0으로 바꿔버리면 어떨까?
                # 다른 경우의 수에 영향을 미쳐서 안되더라
                # data[x][y] = 0
                # visited에 표시해둔 1이 있으면 그 쪽으로 못가게
                visited[nx][ny] = 1

    # x가 99가 된 순간
    if data[x][y] == 2:
        return original_y
    else:
        return '실패'


# 테스트 케이스 10개
# tc는 출력할 입력받은 숫자
for _ in range(10):
    tc = int(input())
    # 100 *100 의 2차원 리스트
    # data =[list(map(int, input().split())) for _ in range(100)]
    data = []
    for i in range(100):
        arr = list(map(int, input().split()))
        data.append(arr)

    # 모든 출발점 찾기
    for i in range(100):
        # 항상 0번째 열에서 출발할거라서 2중포문 필요없음
        # 0번째 열의 i번째 행의 값이 1이면
        if data[0][i] == 1:
            # print(i)  # 모든 출발점
            result = search(0, i)   # 코드 실행 결과 반환값 저장
        # 2인 도착검을 찾은 순간 original_y를 담는 건 맞는데..
        if result != '실패':  # 조사를 한번 끝냈는데,
                        # result에 '실패'말고 다른값이 있다? -> 값 찾았으니가 종료
            break

    print(f'#{tc} {result}')
