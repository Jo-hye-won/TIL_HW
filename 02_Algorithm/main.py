'''
() = 2
[] = 3
(x) = 2 x x
[x] = 3 x x
(xy) = x + y

() [ [] ] => 2 + 3x3 = 11
'''

sentence = input()

stack = []
result = 0
cap = 1

for i in sentence:
    if i == '(':
        cap *= 2
        stack.append(i)

    if i == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            result += cap
            cap //= 2
        else:
            result = 0

    if i == '[':
        cap *= 3
        stack.append(i)
    if i == ']':
        if stack and stack[-1] == '[':
            stack.pop()
            result += cap
            cap //= 3
        else:
            result = 0
if len(stack) != 0:
    result = 0

print(result)
