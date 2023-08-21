import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # data = input().split()
    # arr = []
    # for idx in range(N):
    #     if data[idx].isdigit():
    #         arr.append(int(data[idx]))
    #     else:
    #         arr.append(data[idx])

    # 리스트 컴프리헨션으로 하면
    data = list(map(lambda x : int(x) if x.isdigit() else x, input().split()))
    que = []
    stack = []
    # print(data)
    bonus = 0
    # 전수 조사
    for i in range(N):
        if data[i] == '+':
            bonus += 1
        else:
            data[i] += bonus
            if data[i] % 2 == 0:  # 짝수
                stack.append(data[i])
            else:                 # 홀수
                que.append(data[i])
    # print(B, C)
    # result = 0
    # for j in range(M): # M번의 차례가 올때까지 누적 계산
    #     tmp1 = 0
    #     tmp2 = 0
    #     if stack:
    #         tmp1 = stack.pop()
    #     if que:
    #         tmp2 = que.pop(0)
    #     if i + 1 == M : # 내 차례일 때만 값을 누적시키기
    #         print(tmp1, tmp2)
    #         print(stack, que)
    #         result += tmp1
    #         result += tmp2
    for i in range(M): # M번의 차례가 올때까지 누적 계산
        result = 0
        if stack:
            result += stack.pop()
        if que:
            result += que.pop(0)



    print(f'#{tc} {result}')