import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    when_people = [list(map(int, input().split())) for _ in range(N)]
    when_people.sort()
    # print(when_people)
    result = 'Possible'
    for i in when_people:
        if i <= when_people[i]