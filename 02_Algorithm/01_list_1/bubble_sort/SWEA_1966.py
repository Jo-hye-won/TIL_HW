# bubble_sort

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # bubble_sort(arr, N)

    for i in range(N-1, 0, -1): # i 구간의 마지막 인덱스
        for j in range(i):
            if arr[j] > arr[j+1]: # 왼쪽이 크면
                arr[j], arr[j+1] = arr[j+1], arr[j] # 왼쪽 오른쪽 자리를 바꾸자

    print(f'#{tc}', *arr)
