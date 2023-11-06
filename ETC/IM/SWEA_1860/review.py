import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    when_people = list(map(int, input().split()))
    when_people.sort()
    print(when_people)
    result = 'Possible'
    for i in range(N):
        if i+1 > when_people[i]//M*K:
            result = 'Impossible'
            break
    # print(f'#{tc} {result}')
