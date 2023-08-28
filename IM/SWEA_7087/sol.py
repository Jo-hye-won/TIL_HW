import sys
sys.stdin = open('input.txt')

'''
대회의 문제들에 사용될 수 있는 재목을  N개 만듬

'''
T = int(input())
cnt = 0  # 최대 문제 제목의 개수를 세는 변수

for tc in range(1, T+1):
    N = int(input())
    words = list(input() for _ in range(N))
    print(words)

T = int(input())

for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    ls = []
    for _ in range(N):
        ls.append(input())
        ls.sort()
        # print(ls)
        log = 0
        for i in range(len(ls)-1):
            if log == 0:
                if ord(ls[i][0]) == ord(ls[i+1][0]):
                    cnt += 1
                    log = 1
                if ord(ls[i][0]) + 1 == ord(ls[i+1][0]):
                    cnt += 1
                else:
                    break
            else:
                if ord(ls[i][0]) + 1 == ord(ls[i+1][0]):
                    cnt += 1
                else:
                    break

    print(f'#{tc} {cnt}')