import sys
sys.stdin = open('input.txt')

T = int(input())

# 가로 단어 먼저 탐색하기
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 퍼즐가로세로길이 / 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    word_cnt = 0
    for i in range(N):
        len_cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                len_cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if len_cnt == K:
                    word_cnt += 1
                len_cnt = 0 # 초기화 시켜주기 까먹지 말자

    for a in range(N):
        cnt2 = 0
        for b in range(N):
            if puzzle[b][a] == 1:
                cnt2 += 1
            if puzzle[b][a] == 0 or b == N-1:
                if cnt2 == K:
                    word_cnt += 1
                cnt2 = 0
    print(f'#{tc} {word_cnt}')