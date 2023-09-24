import sys
sys.stdin = open('input.txt')

# N과 M(2)

def dfs(start):
    if len(ls) == M:
        print(' '.join(map(str, ls)))
        return
    for i in range(start, N+1):  # 이거 왜 start하면 되고 1 하면 안돼...?ㅠㅠ
        if visited[i]:
            continue

        visited[i] = True
        ls.append(i)
        dfs(i+1)
        visited[i] = 0
        ls.pop()

N, M = map(int, input().split())
ls = []
visited = [0] * (N+1)
dfs(1)

'''
1 2
1 3
1 4
2 3
2 4
3 4
'''