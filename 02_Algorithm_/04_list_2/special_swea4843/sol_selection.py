import sys
sys.stdin = open('input.txt')

def selection_sort():
    for x in range(10):
        mIdx = x
        for y in range(x + 1, N):
            if x % 2:
                if arr[mIdx] > arr[y]:
                    mIdx = y
            else:
                if arr[mIdx] < arr[y]:
                    mIdx = y
        arr[x], arr[mIdx] = arr[mIdx], arr[x]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    selection_sort()
    result = ' '.join(map(str, arr[:10]))
    print(f'#{tc} {result}')

