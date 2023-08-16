T = int(input())
# ()(((()())(())()))(())
for tc in range(1, T+1):
    gualho = input()
    stack = []   # 빈스택 만들어두고
    pipe = 0     # 잘려진 파이프조각의 총 개수 구할 초기값
    for i in range(len(gualho)):                            # ()는 len개수 더하고 )는 +1해주기  )  (
        if stack:  # 스택안에 값이 존재하면
            if gualho[i-1] == '(' and gualho[i] == ')':  # 스택에 있는 값과 괄호의 값이 조건과같으면
                stack.pop()                     # 스택을 팝한다
                pipe += len(stack)

            elif gualho[i] == ')':
                pipe += 1
                stack.pop()

            else:
                stack.append(gualho[i])

        else:
            stack.append(gualho[i])

    print(f'#{tc}', pipe)