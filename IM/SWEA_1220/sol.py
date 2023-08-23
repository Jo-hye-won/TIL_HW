import sys
sys.stdin = open('input.txt')
'''
1 = N극 성질을 가지는 자성체
2 = S극 성질을 가지는 자성체
테이블의 위쪽에 N극
테이블의 아래쪽에 S극
테이블의 앞뒤쪽에 있는 N극 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.
'''

T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0  # 교착상태 카운트 하기

    for i in range(N):
        status = 0  # 멈춤상태(플래그 변수)
        for j in range(N):
            if table[j][i] == 1:  # 1 움직여
                status = 1  # 움직이고 있어
            elif table[j][i] == 2 and status == 1:  # 2나왔는데 1이 움직이고 있었네?
                cnt += 1  # 교착상태 하나 추가
                status = 0  # 움직임 멈춰
    print(f'#{tc} {cnt}')



