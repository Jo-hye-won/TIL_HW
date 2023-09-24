import sys
sys.stdin = open('input.txt')

# N과 M(1)


def dfs(i):
    if len(ls) == M:
        print(' '.join(map(str, ls)))
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        ls.append(i)
        dfs(i)
        ls.pop()
        visited[i] = 0


N, M = map(int, input().split())
ls = []
visited = [0] * (N+1)
dfs(1)

'''
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3'''