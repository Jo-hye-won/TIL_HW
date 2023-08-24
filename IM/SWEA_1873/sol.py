import sys
sys.stdin = open('input.txt')
'''
전차는 단 하나(^ ∨ < >)

문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)

문자	동작
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
포탄은 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진
강철로된 벽에 부딪히면 아무 일도 안인남
게임 맵 밖으로 포탄이 나가면 아무 일도 안일남
게임맵의 상태가 어떻게 되는지

'''

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())  # 게임 맵의 높이, 너비
    # for _ in range(H):
    #     sentence = input()
    #     print(sentence)

    # H줄만큼 길이가 W인 문자열
    field = [list(input()) for _ in range(H)]
    print(field)

    # 사용자가 넣을 입력의 개수
    N = int(input())
    words = input() # 길이가 N개인 문자열
    # print(words)

    # 탱크 어딨닝
    for i in range(H): # 행 우선 순회
        for j in range(W):
            if field[i][j] == '<' or  field[i][j] == '>' or  field[i][j] == '^' or  field[i][j] == 'v':
                where_tank_i, where_tank_j = i, j
                # print(where_tank_i, where_tank_j)

    # 문자 동작을 하나씩 코드로 옮겨보자
    for word in words:
        print(word)
        if word == 'U':


