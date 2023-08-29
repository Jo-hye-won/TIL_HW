import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    words = input()
    M = len(words)
    N = len(words)//2
    for i in range(len(words)):
        for j in range(N):
            result = 1
            # cnt = 0
            if words[j] != words[M-j-1]:
                result = 0
                break
    print(f'#{tc} {result}')

    # =================================
    # result = 0
    # if words == words[::-1]:
    #     result =1



