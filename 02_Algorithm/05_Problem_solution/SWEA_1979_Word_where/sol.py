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
    N, K = map(int, input().split())  # 퍼즐의 가로,세로길이 / 단어의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0     # 단어가 들어갈 수 있는 자리의 수
    for i in range(N):  # 행 우선 순회
        cnt = 0     # 연속한 빈칸(1)의 개수
        for j in range(N):
            if arr[i][j]:  # True일때 1이라서 ==1 생략 가능
                cnt += 1
            if j == N-1 or arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
    # print(ans)

    # 세로 단어개수도 세어보자
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if i == N-1 or arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f'#{tc} {ans}')



