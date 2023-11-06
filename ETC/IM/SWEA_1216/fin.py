import sys
sys.stdin = open('input.txt')

'''
가장 긴 회문의 길이 

'''
T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    matrix = [input() for _ in range(N)]
    length = 0
    # 회문의 길이 긴것부터 가져와서 l로
    for l in range(N, 0, -1):
        for i in range(N):
            for j in range(N-l+1):
                for k in range(l//2):
                    if matrix[i][j+k] != matrix[i][j+l-1-k]:
                        break
                else:
                    length = max(l, length)
                for p in range(l//2):
                    if matrix[j+p][i] != matrix[j+l-1-p][i]:
                        break
                else:
                    length = max(l, length)
    print(f'#{tc} {length}')