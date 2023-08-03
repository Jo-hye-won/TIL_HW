import sys
sys.stdin = open('input.txt')

# 전체 쪽수 = P
# A가 찾을 쪽 번호 = pa
# B가 찾을 쪽 번호 = pb

T = int(input())


def binary_search(arr, N, ka, kb):
    start = 1   # 시작지점
    end = N     # 끝 지점

    # 시작 지점이 끝 지점보다 작거나 같은 동안
    count_a = 0
    count_b = 0
    while start <= end:
        mid = int((start+end) // 2)
        # count_a = 0
        # count_b = 0

        # A가 몇 번만에 찾는지 도출하기
        if arr[mid] == ka:
            return count_a
        elif arr[mid] > ka:
            end = mid
            count_a += 1
        else:
            start = mid
            count_a += 1

        # B가 몇 번만에 찾는지 도출하기
        if arr[mid] == kb:
            return count_b
        elif arr[mid] > kb:
            end = mid
            count_b += 1
        else:
            start = mid
            count_b += 1

    # 비교해서 출력할 값
    if count_a > count_b:
        return 'B'
    elif count_b > count_a:
        return 'A'
    elif count_a == count_b:
        return 0

    # binary_search(numbers, P, pa, pb)

    # print(f'#{tc} {binary_search(numbers, P, pa, pb)}')


for tc in range(1, T+1):
    P, pa, pb = map(int, input().split())
    numbers = list(range(1, P+1))
    binary_search(numbers, P, pa, pb)
    print(f'#{tc} {binary_search(numbers, P, pa, pb)}')




# for tc in range(1, T+1):
#     P, pa, pb = map(int, input().split())
#     numbers = list(range(P))




    #     mid = (start + end) // 2  # 중앙 인덱스
    #     print(mid, arr[mid])
    #     # 중앙 위치가 내가 찾는 대상이라면
    #     if arr[mid] == key:
    #         return True, arr[mid]
    #     # 아닌데, 중앙 위치 값이 내 키 값보다 크면
    #     elif arr[mid] > key:
    #         end = mid - 1
    #     # 아닌데, 중앙 위치 값이 내 키 값보다 작으면
    #     else:
    #         start = mid + 1
    # return False


    # print(numbers, pa, pb)


# print(f'# ')