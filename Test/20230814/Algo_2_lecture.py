T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []
    # 모든 글자에 대해서 다 조사
    for char in word:
        # 혹시 계속 조사해도 되요..???????
        check = True
        # stack에 넣을 값은 )} 빼고 전부 다
        if char != ')' and char != '}':
            stack.append(char)
        if char not in ')}':
            stack.append(char)
        else:
            if char == ')':
                tmp = 0
                # 스택에 값이 있는 동안
                while stack:
                    val = stack.pop()
                    # val이 정수일 때
                    if val.isdigit():
                        # 값 누적
                        tmp += int(val)
                    # val이 '('일때
                    elif val =='(':
                        # 누적된 값을 스택에 추가
                        stack.append(str(tmp))
                    # val이 '{'일때
                    elif val == '{':
                        # 조사 멈춤
                        check = False  # 이제조사할 필요 없어요
                        break
            elif char == '}':
                tmp = 1
                # 스택에 값이 있는 동안
                while stack:
                    val = stack.pop()
                    # val이 정수일 때
                    if val.isdigit():
                        # 값 누적
                        tmp *= int(val)
                    # val이 '{'일때
                    elif val == '{':
                        # 누적된 값을 스택에 추가
                        stack.append(str(tmp))
                    # val이 '('일때
                    elif val == '(':
                        # 조사 멈춤
                        check = False  # 이제조사할 필요 없어요
                        break
        # 혹시 우리 다음 단어 조사 안해도 되요?
        if check == False:
            break