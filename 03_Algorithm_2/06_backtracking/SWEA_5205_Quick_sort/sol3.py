def quick_sort(arr):
    # 분할
    if len(arr) <= 1:
        return arr
    else:
        # 분할 작업
        pivot = arr[0]
        left, pivot_list, right = [], [], []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            elif arr[i] == pivot:
                pivot_list.append(arr[i])
            else:
                left.append(arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]