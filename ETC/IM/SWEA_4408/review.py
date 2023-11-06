import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # print(rooms)
    cnt = [0] * 201
    for a, b in rooms:
        a = (a + a%2)//2
        b = (b + b%2)//2
        for i in range(min(a,b), max(a,b)+1):
            cnt[i] += 1
    print(f'#{tc} {max(cnt)}')