import sys
sys.stdin = open('sumo.txt')
# 부분합

T = int(input())

# result_list = []

for tc in range(1, T+1):    # 3번 순회하자
    N, M = map(int, input().split())    # 정수의 개수 N
                                     # 더할 구간의 개수 M
    ls = list(input().split())    # 더할 값들을 나눠서 리스트로
    # print(ls) # 리스트 확인!
    '''
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
['6262', '6004', '1801', '7660', '7919', '1280', '525', '9798', '5134', '1821']
['3266', '9419', '3087', '9001', '9321', '1341', '7379', '6236', '5795', '8910', '2990', '2152', '2249', '4059', '1394', '6871', '4911', '3648', '1969', '2176']

    '''
    ls2 = []   # for문 안에서 나올 sums 값을 넣을 빈 리스트를 만들어두고

    for i in range(len(ls)-(M-1)):
        sums = 0    # 반복문 돌때마다 0으로 초기화
                    # ls의 길이에서 (더할구간의 개수(M)-1)만큼 뺀만큼까지의 i 인덱스를 돌려서 반복
                    # 'i'인덱스 자리와 i+1의 자리와 i+2의 자리에 있는 것을 더해야 하니까
                    # 그렇게 세 자리의 수를 더한 값을 sums에 할당해주고
                    # 위에 두줄은 잘못 생각함!
                    # 각 테스트 케이스마다 구간의 개수가 다르기 때문에 M-1로 생각해서 해줘야함
                    # print(i)
        for circle in range(M):
            sums = sums + int(ls[i+circle])
        # i가 0인 상태에서 circle이 0에서 m까지돌면서 sums에 누적적으로 더한 값을 도출해서 ls2에 추가!!
        # 그러고나서 i가 1인 상태로 또 돌고 다음다음 len(ls)-(M-1)-1까지 돈당!

        # print(sums) #sums 값들이 나온거 확인!

    #     # 더해서 나온 sums 값들을 리스트에 담아서
        ls2.append(sums)
    # print(ls2)
    '''
[6, 9, 12, 15, 18, 21, 24, 27]
[29646, 24664, 19185, 27182, 24656, 18558]
[93998, 92908] 이제 나왔다!
    '''

    '''
  # sums 값들이 리스트에 담긴거 확인 => 잘못됐네....?
  [6, 9, 12, 15, 18, 21, 24, 27]
  [14067, 15465, 17380, 16859, 9724, 11603, 15457, 16753]
  [15772, 21507, 21409, 19663, 18041, 14956, 19410, 20941, 17695, 14052, 7391, 8460, 7702, 12324, 13176, 15430, 10528, 7793]
    '''
          # 이제 값들을 비교하자
          # sort 해서(버블정렬로 sort하자)
    for bubble in range(len(ls2)-1, 0, -1):
        for bubble_ in range(bubble):
            if ls2[bubble_] > ls2[bubble_+1]:
                tmp = ls2[bubble_]
                ls2[bubble_] = ls2[bubble_+1]
                ls2[bubble_+1] = tmp
                # if ls2[bubble_] > ls2[bubble_+1]:
                #     ls2[bubble_], ls2[bubble_+1] = ls2[bubble_+1],ls2[bubble_]
    # print(ls2) # ls2 값 잘 정렬된거 확인!
    '''
[6, 9, 12, 15, 18, 21, 24, 27]
[18558, 19185, 24656, 24664, 27182, 29646]
[92908, 93998]

    '''

    # 인덱스 0번째랑 -1번째 값가지고 계산하기
    print(f'#{tc} {ls2[-1] - ls2[0]}')


    # result_list.append(ls2)
    # 내가 이렇게 해둔거는 이중배열 일 때 해야하는 거!!
    # for minmax in range(len(ls2)):
    #     min_max = ls2[minmax][-1] - ls2[minmax][0]
    #     print(min_max)

        # for j in range(len(ls)-2):
        #     ls2.append()

# print(f'#{}{}')

# print(result_list)
# for ls2 in result_list:
#         print(ls2[-1] - ls2[0])


T = int(input())
for _ in range(T):
    rlt = []
    N,M = map(int, input().split())
    num_ls = list(map(int,input().split()))
    c_ls = [sum(num_ls[:i])] for i in range(len(num_ls)+1)]
    for i in range(1, N-M+2):
        rlt.append(c_ls[i+M-1] -c_ls[i-1])
    print(f'#{_+1}',max(rlt)-min(rlt))
