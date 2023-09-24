import sys
sys.stdin = open('input.txt')

# N과 M(4) => 왜 안돼ㅐㅐㅐㅐ

def dfs(s):
    if len(ls) == M:
        print(' '.join(map(str,ls)))
        return

    for i in range(s, N+1):
        ls.append(i)
        dfs(i)
        ls.pop()


N, M = map(int, input().split())
# visited = [0] * (N+1)
ls = []
dfs(1)
