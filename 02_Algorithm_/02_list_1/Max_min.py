# 11092. 최대 최소의 간격

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0  # 최솟값의 인덱스
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:   # 작은것 중 처음꺼
        # if arr[min_idx] >= arr[i]:  # 작은것 중 마지막거
            min_idx = i
        if arr[max_idx] <= arr[i]:  # 큰것 중 마지막꺼
            max_idx = i
    # print(min_idx)
    # print(max_idx)
    ans = max_idx - min_idx
    if ans < 0:
        print(abs(ans))
    else:
        print(ans)