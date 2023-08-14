def bubble_sort(numbers):
    # n-1 번째까지 조사를 해나갈 것
    # range(start, end, step)
    # -> 작성된 정수부터 시작
    # -> end : 작성된 정수 - step까지
    # -> step : 다음 정수의 값
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            # print(numbers[j], numbers[j+1])
            if numbers[j] > numbers[j+1]:
            # 둘의 값을 바꿔치기 한다
            # tmp = numbers[j]
            # numbers[j] = numbers[j+1]
            # numbers[j + 1] = tmp
                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                 # print(numbers, numbers[j], numbers[j+1])
    return numbers
numbers= [58, 7, 78, 12, 42]
print(bubble_sort(numbers))
# print(numbers)

# 내림차순 해보기!!
numbers2= [58, 7, 78, 12, 42]
def Bubble_sort(numbers2):
    for i in range(len(numbers2)):
        for j in range(len(numbers2)-1, i, -1):
            if numbers2[j]>numbers2[j-1]:
                numbers2[j], numbers2[j - 1] = numbers2[j-1],  numbers2[j]
    return numbers2

print(Bubble_sort(numbers2))
# print(numbers2)