import sys
sys.stdin = open('input.txt')

'''
포장할 수 없는 경우 -1
포장할 수 있는 경우 : 상자에 들어있는 당근의 개수 차이가 최소일 때의 차이값
<조건 5개>
1. 대 중 소 상자로 구분해서 포장
2. 같은 크기의 당근은 같은 상자에 들어있어야
3. 비어있는 상자가 있으면 안됨
4. N/2개 초과하는 당근 있으면 안됨
5. 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장
# '''
def check(N, ls): # 당근의 크기를 입력하면 모든 조건을 확인하는 프로그램
    '''
    당근 3개 => 소,중,대 상자에 든 당근의 개수 차이 = 0 소 1 중 1 대 1 씩 들어갔으니까
    당근 5개  > 소 3 중 1 대 1 = 당근의 개수 차이 2
        그런데 2개 초과하는 상자 잇으니까 조건 만족 x
    당근 8개
    '''
    L = int(N/2) # L초과하는 당근이 있으면 안됨
    ls.sort()
    min_chai = 987654321  # 포장개수차이 최소값 초기값 설정
    for i in range(N-2):
        for j in range(i+1, N-1):
            if ls[i] != ls[i+1] and ls[j] != ls[j+1]:
                small = i+1
                middle = j-i
                large = N-1-j
                if small <= L and middle <= L and large <= L:
                    if min_chai >= (max(small, middle, large) - min(small, middle, large)):
                        min_chai = max(small, middle, large) - min(small, middle, large)
    return min_chai

T = int(input()) # 수확횟수
for tc in range(1, T+1):
    N = int(input()) # 수확한 당근의 개수 3
    C = list(map(int, input().split())) # 당근의 크기 1 2 3
    # C.sort() # 당근을 크기 순으로 정렬
    # min_v = 1000 # 포장별 최소 개수 차이, 포장 불가인 경우 -1
    # for i in range(N-2):
    #     for j in range(i+1, N-1):
    #         if C[i] != C[i+1] and C[j] != C[j+1]: # 같은 크기 사이에 경계를 두면 안돼
    #             small = i + 1   # 소 상자에 들어간 당근 개수
    #             middle = j-i    # 중 상자에 들어간 당근 개수
    #             large = N-1-j   # 대 상자에 들어간 당근 개수
    #             if 0 < small <= N//2 and 0 < middle <= N//2 and 0 < large <= N//2:
    #                 if min_v > (max(small, middle, large) - min(small, middle, large)):
    #                     min_v = max(small, middle, large) - min(small, middle, large)
    res = check(N,C)
    if res == 987654321:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {res}')
    # if min_v == 1000: # 포장할 수 없어서 갱신되지 않은 경우
    #     min_v = -1 # -1 출력해라
    # print(f'#{tc} {min_v}')

    # # 대,중,소 상자로 구분
    # big = []
    # middle = []
    # small = []
    #
    #
    # if N == 3:
    #     small.append(ls.pop(0))
    #     middle.append(ls.pop(0))
    #     big.append(ls.pop(0))
#
#