import sys
sys.stdin = open('input.txt')

T = 10
N = 100

for _ in range(1, T+1):
    tc = int(input())
    pallin = [input() for _ in range(N)]
    # print(pallin)
    long = 1

    for K in range(N, 0, -1): # K의 길이를 긴 것부터 뽑아와서 설정해주고
        for i in range(N):
            for j in range(N-K+1):
                for k in range(K//2):
                    check = True
                    if pallin[i][j+k] != pallin[i][j+K-1-k]:
                        check = False
                        break
                if check:
                    # 설정해둔 K랑 long이랑 비교해서 가장 긴 회문길이 구하기
                    long = max(long, K)

                for p in range(K//2):
                    check = True
                    if pallin[j+p][i] != pallin[j+K-1-p][i]:
                        check = False
                        break
                if check:
                    long = max(long, K)
    print(f'#{tc} {long}')


