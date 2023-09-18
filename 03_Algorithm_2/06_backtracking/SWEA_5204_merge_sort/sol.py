import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    # 분할 종료 시점
    if len(arr) <= 1:
        return arr

    # 중앙 위치
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 분할 종료 시점이 될 때까지 계속 쪼개기
    left = merge_sort(left)
    right = merge_sort(right)

    # 분할 완료 후, 병합하기 위한 과정
    # 왼쪽 리스트의 0번 인덱스와
    # 오른쪽 리스트의 0번 인덱스 값 비교

    # 그 중, 작은 값을 (오름차순 정렬 할거니까) 먼저 어딘가에 담거나, 원본에 넣거나
    left_index, right_index, k = 0, 0, 0
    # 좌, 우 정렬 시도
    # k => 원본에서 교체되어야 될 위치 index
    while left_index < len(left) and right_index < len(right):
        # 오른쪽이 더 크면
        if left[left_index] < left[right_index]:
            # 원본 배열의 k번째에 더 작은 값인 left 삽입
            arr[k] = left[left_index]
            left_index += 1


            # 왼쪽이 더 크면
        else:
            arr[k] = right[right_index]
            right_index += 1
        # 다음 원본 조사 위치로 이동
        k += 1
    # 모든 조사 완료후, 아직 남아있는 값이 있을 수 있다.
    # 남아 있는 경우는
    if left_index < len(left):
        arr[k:] = left[left_index:]
    if right_index < len(right):
        arr[k:] = right[right_index:]

    if left[-1] > right[-1]:
        result += 1

    return arr



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {result}')