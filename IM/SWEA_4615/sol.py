import sys
sys.stdin = open('input.txt')
'''
돌의 색이 1이면, 흑돌
돌의 색이 2이면, 백돌

'''
def f(i, j, bw, N):
    game_board[i][j] = bw # 주어진 돌 놓기
    for di, dj in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]:
        ni, nj = i + di, j + dj
        tmp = [] #
        # 보드 내부이고 반대색이면 계속 이동
        while 0 <= ni < N and 0 <= nj < N and game_board[ni][nj] == op[bw]:
            tmp.append((ni,nj))
            ni, nj = ni+di, nj+dj
        # 보드 내부이고 같은색이면
        if 0 <= ni < N and 0 <= nj < N and game_board[ni][nj] == bw:
            for p, q in tmp:
                game_board[p][q] = bw

B = 1 # 흑돌 1
W = 2 # 백돌 2
op = [0,2,1] # 보드의 반대 색

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 보드 한 변의 길이 N / 돌을 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]
    game_board = [[0]*N for _ in range(N)]  # 좌표 인덱스 사용: 0 -> N-1까지
    # 중심부에 4개의 돌 기본 배치하기
    game_board[N//2-1][N//2-1] = W
    game_board[N//2-1][N//2] = B
    game_board[N//2][N//2-1] = B
    game_board[N//2][N//2] = W
    # 입력이 col, row, color 순으로 되어있음(col과 row는 인덱스 1 기준)

    for col, row, color in play:
        f(row-1, col-1, color, N)  # 함수를 만들어 볼거다 (돌 놓기)

    # 각 테스트 케이스마다 게임이 끝난 후! 보드 위의 흑돌, 백돌의 개수를 출력한다.
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == B:
                bcnt += 1
            elif game_board[i][j] == W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')
