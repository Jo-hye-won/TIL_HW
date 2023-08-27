import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    # print(N,K)
    # print(scores)
    scores.sort()  # 정렬 해주고
    sum_ls = []  # 최대값 K개 넣을 리스트 만들고
    for i in range(K):
        sum_ls.append(scores.pop()) # 정렬해둿으니까 뒤에서부터 큰 수 K개
                            # pop해서 리스트에 넣어주고
    # print(sum_ls)

    result = 0 # 결과값 변수
    for j in range(len(sum_ls)): # 리스트에 넣은 개수만큼 반복하면서
        result += sum_ls.pop() # 결과값에 누적해서 더해주기

    print(f'#{tc} {result}')