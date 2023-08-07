T = int(input())

for t in range(T):
    tc = list(input())
    result = tc[0]+tc[-1]

    print(''.join(result))