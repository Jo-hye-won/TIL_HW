# 재귀

# arr : 원본 배열
# N : 배열의 길이
# key : 타겟
# start : 시작지점
# end : 끝지점

def binary_search(arr, N, key, start, end):
    if start > end:  # 시작지점이 끝지점보다 커지면
        # 타겟 찾을 수 없음 ==> 조사 종료
        return False
    else:
        mid = (start + end) // 2
        print(mid, arr[mid])
        if arr[mid] == key:
            return True, arr[mid]
        elif arr[mid] > key:
            end = mid - 1
            return binary_search(arr, N, key, start, end)
        else:
            start = mid + 1
            return binary_search(arr, N, key, start, end)
    # return False


numbers=list(range(1,30,2))

N = len(numbers)
target = 25

print(binary_search(numbers, N, target, 0, N-1))