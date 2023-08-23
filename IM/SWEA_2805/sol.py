import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    non = [list(map(int, input().split())) for _ in range(N)]
    print(non)

'''
# 오른쪽으로 순회하면서 가운데부터 +1씩 늘리고
범위가 가운데가 되면 -1씩 count 
'''
Test = int(input())
for test in range(Test):
    farm_size = int(input())
    farm_info = [list(map(int, input())) for _ in range(farm_size)]
    ans = 0
    for i in range(farm_size):  # i in range(4) i = 0,1,2,3
        start = farm_size//2 - i  # start =2-0/1/2/3 => 2,1,0,-1
        end = farm_size//2 + i + 1  # end  = 2+0/1/2/3+1 => 3,4,5,6
        if start < 0: # -1
            start = -start # 1
        if end > farm_size: # 3 >2
            end = farm_size * 2 - end  # 6-3=3
        for j in range(start, end):  # 1,3
            ans += farm_info[i][j]

    print(f'#{test+1} {ans}')