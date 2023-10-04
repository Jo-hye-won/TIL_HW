import sys
sys.stdin = open('input.txt')

N = int(input())
people = []
for _ in range(N):
    x, y = map(int, input().split())
    # print(x, y)
    people.append([x,y])
# print(people)
# cnt = 0
# print(len(people))
# P = len(people)
for per in people:
    cnt = 1
    for per_two in people:
        if per[0] < per_two[0] and per[1] < per_two[1]:
            cnt += 1
    print(cnt, end=' ')