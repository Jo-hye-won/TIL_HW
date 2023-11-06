import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 입력받는다
T = int(input())

# 테스트 케이스만큼 반복한다
for t in range(1, T+1):
    # 입력을 받아 퍼즐 모양을 저장한다
    N, K = map(int, input().split())
    # print('N', N)  # 가로, 세로 길이 N
    # print('K', K)  # 단어의 길이 K
    puzzle = []
    for n in range(N):
        puzzle.append(input().split())
    print()
    for p in puzzle:
        print(*p)
    print()
    # 자리의 수를 카운트할 변수를 준비한다 (cnt)
    cnt = 0
    # i, j의 이중 포문으로 탐색을 한다
    # 각각 가로, 세로 0 ~ N 까지 탐색
    for i in range(N):
        for j in range(N):
            print(i, j, sep=',')
            # 가로 방향과 세로 방향의 탐색을 K+1까지 각각 진행하되
            # 1. 탐색 중 0을 만나거나 벽을 넘어가면 continue
            # 2. K까지 탐색 완료 후, K+1이 범위를 벗어나거나, 0(검은색)이라면 cnt+=1

            # 행 방향 탐색 (세로 탐색 - 리스트)
            print('행 방향 탐색 (세로)')
            # 직전이 벽이거나, 닫혀 있을 때만 탐색 진행
            # TODO : 탐색 로직

            # 열 방향 탐색 (가로 탐색 - 리스트 안 리스트)
            print('열 방향 탐색 (가로)')
            # 직전이 벽이거나, 닫혀 있을 때만 탐색 진행
            # TODO : 탐색 로직

    # 자리의 수를 출력한다
    print('cnt', cnt)