T = int(input())

for tc in range(1, T+1):
    # 버스 노선 N
    N = int(input())
    # i 번째 버스 노선 Ai이상
    # Bi 이하인 모든 정류장만 다니는 버스 노선
    li = []
    for _ in range(1, N+1):
        A, B = map(int, input().split())
        li.append((A, B))
        # print(li)

    # P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는
    P = int(input())
    li2 = [0] * P
    for i in range(P):
        C = int(input())
        for a, b in li:
            if a <= C <= b:
                li2[i] += 1

    print(f'#{tc}', *li2)