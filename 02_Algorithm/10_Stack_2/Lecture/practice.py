# 2+3*4/5

cal = '2+3*4/5'
# 최종 결과값
result = ''    # 빈 문자열
# 연산자들을 모아 둘 스택
stack = []

# 전수조사
for char in cal:
    # 연산자가 아닌 경우(정수인 경우)
    if char not in '+-*/':
        result += char
    else:
        stack.append(char)

# stack 에 들어있는 모든 연산자들을 result에 더해주려면
while stack:
    result += stack.pop()
print(result, stack)