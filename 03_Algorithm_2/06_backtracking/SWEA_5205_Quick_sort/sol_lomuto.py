import sys
sys.stdin = open('input.txt')

def quick_sort(arr, left, right):
    # 분할 정복의 가장 핵심
    # 정복 대상의 범위를 가장 작아질 때까지 계속 쪼갠다.
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


# lomuto => 피봇을 가장 오른쪽 원소로 결정
def cal(arr, left, right):
    # i는 피봇보다 큰 구간의 왼쪽 경계
    i = left - 1
    # j는 피봇보다 큰 구간의 오른쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        # pivot이 j번째 값보다 더 크면
        if pivot > arr[j]:
            i += 1
            # i와 j 사이구간에 피봇보다 큰 값이 있다!!
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    # print(left, right)
    # print(arr)
    return i + 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    # print(arr)
    print(f'#{tc} {arr[N // 2]}')
