import sys
sys.stdin = open('input.txt')
'''
파리는 죽기 전까지 몇 마일의 거리를 이동했을까?
'''

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # A와 B는 D/(A+B)시간이면 만난다
    time = D/(A+B)

    # 파리의 이동거리은 D/(A+B)를 파리의 속력이랑 곱하면 된다
    result = time*F
    print(f'#{tc} {result}')




