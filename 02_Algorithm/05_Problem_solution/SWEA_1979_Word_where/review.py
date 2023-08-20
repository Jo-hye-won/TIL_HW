import sys
sys.stdin = open('input.txt')
'''
흰색부분(1) = 단어가 들어갈 수 있는 부분
검은부분(0) = 단어가 들어갈 수 없는 부분
N = 퍼즐의 가로, 세로 길이
K = 단어의 길이
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    word_puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 가로단어 먼저 찾아보자(행우선 순회)
    # 넣을 수 있는 단어의 개수
    words = 0
    for i in range(N):
        cnt = 0  # 단어의 길이(한 행 순회할때마다 다시 세어줘야해서 여기서 초기화)
        for j in range(N):
            # 1을 만나면 단어을 넣을 수 있어서 cnt += 1해준다
            if word_puzzle[i][j] == 1:
                cnt += 1
            # 끝까지 다 갔거나 검은부분을 만나서 탐색이 끝나고
            if j == N-1 or word_puzzle[i][j] == 0:
                # 그 때의 가로로 단어의 길이(cnt)가 K인 경우
                if cnt == K:
                    words += 1  # 넣을 수 있는 단어 찾았다!(+1)
                    # 넣을수 있는 단어 찾았으니까 또 다음 단어 찾기 위해서
                # if문 끝나면!! cnt 다시 0으로 초기화 해두기
                cnt = 0   # if문 안에 넣어두면 안돼ㅐㅐ

    # 세로단어 찾아보자(열우선 순회)
    for k in range(N):
        cnt2 = 0
        for l in range(N):
            if word_puzzle[l][k] == 1:
                cnt2 += 1
            if l == N-1 or word_puzzle[l][k] == 0:
                if cnt2 == K:
                    words += 1
                cnt2 = 0
    print(f'#{tc} {words}')




