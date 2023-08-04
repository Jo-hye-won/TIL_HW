import sys
sys.stdin = open('input.txt')

# 특별한 정렬

T = int(input())
max_min = []

def bubble_sort():
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
               numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for tc in range(1, T + 1):
    N = int(input())
    num = map(int, input().split())
    numbers = list(num)
    bubble_sort()
    # print(numbers)
    max_min = []
    # while len(numbers) != 0:
    for j in range(5):
    # for j in range(len(numbers)//2):
        max_min.append(numbers.pop())
        max_min.append(numbers.pop(0))
    # print(max_min)

    # join은 문자열을 받아서 하는 애라서 max_min을 문자열로 바꿔서 해야함
    # result_str = " ".join(map(str, max_min))
    # print(result_str)

    print(f'#{tc}',*max_min)
    # result = numbers[:10]
    # print(result)
    #
    # max_min = []
    # while len(result) != 0:   # 종료조건을 잘 생각하자..... == 이 아니라 != 해야한다.
    # # for j in range(10):
    #     max_result = result.pop(-1)
    #     # max_min.append((result.pop()))
    #     min_result = result.pop(0)
    #     # max_min.append((result.pop(0)))
    #     # print(max_result, min_result)
    #     max_min.append(max_result)
    #     max_min.append(min_result)
    # # print(max_min)
    #
    # print(f'#{tc}',*max_min)

    # print(f'{tc} {numbers}')
'''
1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2 [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
3 [3, 9, 17, 18, 21, 26, 30, 36, 43, 46, 59, 60, 62, 64, 69, 71, 75, 88, 97, 98]
'''
    # print(result) # 정렬하고 슬라이싱 하고 큰값작은값을 뽑는게 아니라 큰값작은값을 뽑은 다음에 10개 슬라이싱 해야함.
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
[3, 9, 17, 18, 21, 26, 30, 36, 43, 46]
'''


