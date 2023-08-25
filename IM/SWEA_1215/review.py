import sys
sys.stdin = open('input.txt')

T = 10
N = 8

for tc in range(1, T+1):
    M = int(input())  # 찾아야 하는 회문의 길이
    arr = [input() for _ in range(N)]
    word_cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M // 2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                word_cnt += 1

            for p in range(M //2):
                if arr[j+p][i] != arr[j+M-1-p][i]:
                    break
            else:
                word_cnt += 1
    print(f'#{tc} {word_cnt}')

