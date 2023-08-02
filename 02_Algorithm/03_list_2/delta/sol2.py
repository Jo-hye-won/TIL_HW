import sys
sys.stdin = open("input.txt")


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
Testcase = int(input())
for tc in range(Testcase):
    N = int(input())
    List = [list(map(int, input().split())) for _ in range(N)]

    final = 0
    for i in range(N):
        for j in range(N):
            sums = 0
            center = List[i][j]
            compare_list = []
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if (0<=ni<N) and (0<=nj<N):
                    compare_list.append(List[ni][nj])
            for com in compare_list:
                sums += abs(com-center)
            final += sums
    print(f'#{tc+1} {final}')