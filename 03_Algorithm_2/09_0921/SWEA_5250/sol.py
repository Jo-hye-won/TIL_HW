import sys
sys.stdin = open('input.txt')
# 최소 연료 소비량을 출력하는 프로그램
import collections import deque

dx = []
dy = []



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Hs = [list(map(int, input().split())) for _ in range(N)]
    print(Hs)

    # 비교대상
    max_val = sum(sum(Hs, [])) + N**2  # 이거 무슨말이지
    # print(result)
    # 이전에 방문한 적이있다면, 가중치를 visited에 기록
    # 최초 방문시에도 비교할 수 있는 값이어야 한다. -> 최소비용을 찾고 있으므로

    visited = [[max_val] * N for _ in range(N)]


    # print(f'#{tc} {result}')