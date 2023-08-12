T = 10

for tc in range(1, T+1):
    N, contents = input().split()
    # print(N, contents)
    # contents_ls = list(contents)
    # 문자열은 인덱스 번호 쓸 수 있어서 굳이 리스트로 바꿔줄 필요없음
    stack = []
    for i in range(int(N)):      # 문자열 길이만큼 순회하면서
        if len(stack) == 0:      # 스택에 값이 없으면
            stack.append(contents[i])  # 값을 넣어주고

        else:  # 값이 있으면
            if stack[-1] == contents[i]:  # 똑같은지 비교하자
                stack.pop()  # 똑같으면 스택에서 제거하기
            else:
                stack.append(contents[i])   # 다르면 추가해주기

    print(f'#{tc}', end=' ')
    for j in stack:   # 같은건 제거되고 다른건 추가되서 남은 비밀번호
                      # 하나씩 꺼내와서 출력
        print(j, end='')
    print()