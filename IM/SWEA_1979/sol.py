import sys
sys.stdin = open('input.txt')

'''
흰색 부분 = 1 (단어 들어갈 수 있는 곳)
검은색 부분 = 0  (단어 들어갈 수 없는 곳)

'''
T = int(input())

# 가로 단어 먼저 탐색하기
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 퍼즐가로세로길이 / 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(puzzle)
    words = 0  # 들어갈수 있는 단어의 개수
    # 가로로 순회하면서 흰색부분이 나오면 cnt +1 하고
    for i in range(N):
        cnt = 0  # 단어의 길이
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
                # print(cnt)
                # 하다가 0을 만나거나 퍼즐의 끝이나오면 멈추고
            if puzzle[i][j] == 0 or j == N-1:
                # 그 때의 길이를 단어의 길이 K와 비교해서
                if cnt == K:
                    # 길이가 같으면 들어갈 수 있는 단어 +1 해주기
                    words += 1
                cnt = 0  # 카운트 다한다음에 다시 다음 단어 길이 세려면
                #         # 초기화 다시 해줘야 하는데 자꾸 까뮤금
    # print(words,'words')

    for a in range(N):
        cnt2 = 0
        for b in range(N):
            if puzzle[b][a] == 1:
                cnt2 += 1
            if puzzle[b][a] == 0 or b == N-1:
                if cnt2 == K:
                    words += 1
                cnt2 = 0
    print(f'#{tc} {words}')




