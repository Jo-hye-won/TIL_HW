import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    length = len(arr)//2

    # print(length)
    ls = []
    count = 0
    for i in range(length):
        for j in range(N-M+1):
            if arr[i] == arr[length-1-i]:
                count += 1
            if count == M:
                ls.append(arr[i])
                print(arr[i])



