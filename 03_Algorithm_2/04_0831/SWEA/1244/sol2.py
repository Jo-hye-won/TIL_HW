import sys
sys.stdin = open('input.txt')


def perm(now, r):
    global result
    val = int(''.join(cards))
    # print(val)
    # 중복제거
    # now번째에 만들어진 어떤 수
    if val in visited[now]:
        return
    visited[now].add(val)
    if now == r:
        if result < val:
            result = val
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                cards[i], cards[j] = cards[j], cards[i]
                perm(now+1, r)
                cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(1, 5):
    cards, r = list(map(int, input().split()))
    cards = list(str(cards))
    visited = [set() for _ in range(11)]
    N = len(cards)
    # R번째일 때, 만들어질 수
    result = 0
    perm(0, r)
    print(visited)