import sys
sys.stdin = open('input.txt')

def bubble_sort():
    for x in range(N):
        for y in range(N-1, x, -1):
            if x % 2:
                if arr[x] > arr[y]:
                    arr[x], arr[y] = arr[y], arr[x]
            else:
                if arr[x] < arr[y]:
                    arr[x], arr[y] = arr[y], arr[x]
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    bubble_sort()
    result = ' '.join(map(str, arr[:10]))
    print(f'#{tc} {result}')
