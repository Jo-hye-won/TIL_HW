import sys
sys.stdin = open('input.txt')

# N과 M(1)

def dfs():
    if len(ls) == M:
        print(' '.join(map(str, ls)))
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        ls.append(i)
        dfs()
        ls.pop()
        visited[i] = 0



N, M = map(int, input().split())
ls = []
visited = [0] * (N+1)
dfs()