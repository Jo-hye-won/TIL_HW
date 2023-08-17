import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    whaduck = deque([])
    cheeses = deque(input().split())
    cheese_idx = deque([])

    idx = 1
    while cheeses:
        cheese_idx.append([cheeses.popleft(), idx])
        idx += 1

    for _ in range(N):
        whaduck.append(cheese_idx.popleft())

    while whaduck:
        first = whaduck.popleft()  # 리스트로 된 피자의 정보를 받아서
        first[0] = int(first[0])//2
        if not first[0]:
            if cheese_idx:
                whaduck.append(cheese_idx.popleft())
        else:
            whaduck.append(first)

    print(f'#{tc} {first[1]}')



#