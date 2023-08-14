cal = '2+3*4/5'
# 최종 결과값
result = ''    # 빈 문자열
# 연산자들을 모아 둘 스택
stack = []

# 전수조사
for char in cal:
    # 연산자라면
    if char in '+-*/()':
        # print(char, '연산자')
        # 연산자 우선 순위에 맞춰서 stack 넣거나 빼거나
        # 우선 순위가 높은 순으로 조건문 처리
        if char == '(':
            stack.append(char)  # 우선순위 제일 높으므로 그냥 추가(push)
        elif char in '*/':  # 마지막 값이 나와 같은 */일 때까지
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)

        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

    else:   # 정수면 result에 더해버리면 된다.
        result += char
while stack:
    result += stack.pop()
print(result)
