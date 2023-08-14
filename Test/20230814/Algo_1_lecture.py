T = int(input()) # => 3개

    # 상  우  하  좌 비교할 위치 좌표로 옮겨가기 위한 설정
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):  # T만큼 반복하면서
    N = int(input())  # 지도의 가로세로 크기 = N
    # N개의 줄에 걸쳐서 N개의 높이 h 주어짐  # h들이 모여있는 리스트 배열 만들기
    data =[]
    for _ in range(N):
        data.append(list(map(int, input().split())))
        # data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for now_col in range(N):
        for now_raw in range(N):
            for k in range(4):
                new_col_position = now_col + di[k]
                new_raw_position = now_raw + dj[k]
                # 범위를 벗어나지 않았을때에만 다음 조사
                if 0 <= new_col_position < N and 0 <= new_raw_position < N:
                    # 다음 조사 위치가 어떠해야하는가?
                    # 상하좌우 조사중에 나보다 크거나 같은 애가
                    # 하나라도 있으면 봉우리조건 만족 못하니까
                    # 더이상 조사할 필요가 없음

