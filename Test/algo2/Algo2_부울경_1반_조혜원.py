T = int(input())  # 테스트케이스 수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    # 최종 결과값
    result = 0
    for i in range(1, N+1):
        for x in range(0, N, i):
            result += arr[x]

    if result < 0:
        result = 0
print(f'#{tc} {result}')


    # result = 0
    # for x in range(0, N, 1):
    #     result += arr[x]
    #
    # for x in range(0, N, 2):
    #     result += arr[x]
    #
    # for x in range(0, N, 3):
    #     result += arr[x]
    #
    # for x in range(0, N, 4):
    #     result += arr[x]











    # tmp = [0] * len(case)  # 값을 구해서 더할 배열 만들어두기
    # # print(tmp)