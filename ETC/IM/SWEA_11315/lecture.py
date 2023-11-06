import sys
sys.stdin = open('input.txt')

def search(bd):
    # i, j의 이중 포문으로 탐색을 한다
    # 각각 가로, 세로 0 ~ N-1 까지 탐색
    for i in range(N):
        for j in range(N):
    # 1) 현재 위치(i,j)에 돌이 존재?
        if bd[i][j] != 'o':
            # 돌이 존재하지 않을 때 다음 점 탐색을 하게 해두자
            continue
        else:

    # 우측 탐색, 좌측 탐색, 우하측 탐색, 좌하측 탐색

    # 2) 각 탐색의 끝점이 범위 안?
    # 3) 혹시 탐색 중 '.'을 만남? (돌 없음)
    # 1,2,3 통과 시 탐색 종료 후 YES 출력

    # 우측탐색 ( i -> 위아래, j -> 왼쪽 오른쪽과 관련있음)
    if j + 5 <= len(bd):  # 이 범위 안에 있다면 우측탐색이 가능하다
        for b in board[i][j+1:j+5]  # i는 고정하고, j만 이미 탐색한 j 말고 j +1부터 j+4까지 탐색
            if b == '.':
                break
        else: # 중간에 흐름제어 없이 잘 for문이 끝나면
            return True  # 더 이상 돌지 말고 함수 자체를 끝내서 YES를 리턴해라


    # 하측탐색
    if i + 5 <= len(bd):
        for b in board[i+1: i+5]:
            b
            for b2 in b1:

        else: # 중간에 흐름제어 없이 잘 for문이 끝나면
            return True  # 더 이상 돌지 말고 함수 자체를 끝내서 YES를 리턴해라

    # 우하측탐색
    if i + 5 <= len(bd) and j + 5 <= len(bd):

    # 좌하측탐색
    if i + 5 <= len(bd) and j - 5 <= len(bd):


# 테스트 케이스를 입력받는다

# 테스트 케이스만큼 반복한다
T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N = int(input())

    # 입력을 받아 바둑판 모양을 저장한다 (board)
    board = []
    for _ in range(N):
        board.append(input().strip())# 여백을 없애주는 작업(.strip)
        # 꼭 해야하는게 아니고, 문제 풀다보면 여백(스페이스)이 달려들어가는 경우가 있음

    # 탐색해도 아무 것 없으면 False