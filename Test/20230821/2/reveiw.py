import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = input().split()
    arr = []
    for i in data:
        if i.isdigit():
            arr.append(int(i))
        else:
            arr.append(i)
    # print(arr)
    result = 0
    que = []
    stack = []
    bonus = 0
    for j in arr:
        if j == '+':
            bonus += 1
        else:
            j += bonus
            if j % 2 == 1:  # 홀수면
                que.append(j)
            else:           # 짝수
                stack.append(j)
    # print(que)
    # print(stack)

    for k in range(M): # 나의 순서까지
        result = 0
        if que:
            result += que.pop(0)
        if stack:
            result += stack.pop()

    print(f'#{tc} {result}')

        # while que and stack:
        #     result = 0
        #     result += que.pop(0)
        #     result += stack.pop()
