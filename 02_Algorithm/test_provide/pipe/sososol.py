T = int(input())

for t in range(1, T + 1):
    pipe = list(input())

    lst = []
    cnt = 0
    for i in range(len(pipe)):
        lst.append(pipe[i])
        if pipe[i] == ')' and pipe[i - 1] == '(':
            lst.pop()
            lst.pop()
            cnt += len(lst)

        elif pipe[i] == ')':
            lst.pop()
            lst.pop()
            cnt += 1
    print(f'#{t} {cnt}')