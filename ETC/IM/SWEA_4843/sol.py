import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(numbers)
    result = []
    numbers.sort()
    # print(numbers)
    while numbers:
        result.append(numbers.pop())
        result.append(numbers.pop(0))

    case = result[:10]

    print(f'#{tc}',*case)
    # print(result)
    # print(numbers)