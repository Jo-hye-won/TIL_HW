import sys
sys.stdin = open('input.txt')

'''
1 = N극
2 = S극
'''
T = 10

for tc in range(1, T+1):
    N = int(input()) # 테이블의 한 변의 길이
    table = [list(map(int, input().split())) for _ in range(N)]
    # print(table)
    cnt = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if table[j][i] == 1:
                flag = 1
            elif table[j][i] == 2 and flag == 1:
                cnt += 1
                flag = 0 # 다시 아무것도 안움직이는 상태로 되돌려주기
    print(f'#{tc} {cnt}')
