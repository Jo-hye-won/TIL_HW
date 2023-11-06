import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = 8
    K = int(input()) # 찾아야 하는 회문 길이
    map = [input() for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N-K+1): # 회문의 길이가 K라서
            for k in range(K//2): # 찾아야 하는 회문길의의 절반만큼 기준잡아서
                if map[i][j+k] != map[i][j+K-1-k]: # 가로 회문
                    break  # 회문이 아니면 끝내고
            else:  # 회문이면
                cnt += 1  # 개수 +1 해주기

            for p in range(K // 2): # 세로 회문
                if map[j+p][i] != map[j+K-1-p][i]:
                    break
            else:
                cnt += 1
    print(cnt)


