import sys
sys.stdin = open('input.txt')

def rotation_90(arr):
    matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix[i][j] = arr[N-1-j][i]
    return matrix


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = rotation_90(arr)
    result2 = rotation_90(result)
    result3 = rotation_90(result2)
    # print(result)

    print(f'#{tc}')
    for k in range(N):
        a = map(str, result[k])
        b = map(str, result2[k])
        c = map(str, result3[k])
        print(''.join(a), ''.join(b), ''.join(c))