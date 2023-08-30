import sys
sys.stdin = open('input.txt')
'''
<output>
False
True
True
False
'''
# row : 현재 조사 대상
# chosen : 선택 대상
# 완전 검색을 할거다
 # 모든 N개의 원소를 다 조사헀는지 판단

def perm(row, chosen):
    if row == N:
        tmp = []
        for i in chosen:
            tmp.append(chosen[i])

        print(chosen)
        return

    # 모든 N개의 원소를 조사 했는지 판단
    for i in range(N):
        # i번째 쓰겠다고 이전에 판정된 적이 있디면,
        # 현재 조사 대상을 i번째에 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[row] = i # row번째 대상을 i번째에 둬서 사용하겠다.
        perm(row + 1, chosen) # 다음 조사를 하러 가기
        chosen[row] = -1


for tc in range(1, 5):
    N = 6
    data = input()
    # i번째에 들어갈 수 있는 수 0, N-1까지를 제외한
    chosen = [-1] * N
    perm(0, chosen)