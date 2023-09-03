
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    numbers, count = input().split()
    # print(numbers,count)
    count = int(count)

    # print(set(numbers),'set')
    # print(set([numbers]))
    nums = set([numbers])
    SET = set()
    # print(nums)

    for _ in range(count):
        while nums:
            n = nums.pop()
            # print(n)
            n = list(n)
            # print(n)
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    # print(i,j)
                    # print(n[i], n[j])
                    n[i], n[j] = n[j], n[i]
                    SET.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
        nums, SET = SET, nums

    result = max(nums)
    print(f'#{t} {result}')