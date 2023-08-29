import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(1, N+1):
    cnt = 0
    a = str(i)
    # print(type(i))
    if '3' in a:
        cnt += a.count('3')
    if '6' in a:
        cnt += a.count('6')
    if '9' in a:
        cnt += a.count('9')
        # print(cnt)
    if cnt >= 1:
        leng = cnt
        res = '-' * leng
    else:
        res = i
    print(res, end=' ')

''' 축약하면

N = int(input())
for i in range(1, N+1):
    i = str(i)
    if '3' in i or '6' in i or '9' in i:
        clap = i.count('3') + i.count('6') + i.count('9')
        for _ in range(clap):
            print('-', end='')
        print(' ', end='')
    else:
        print(i, end=' ')
'''