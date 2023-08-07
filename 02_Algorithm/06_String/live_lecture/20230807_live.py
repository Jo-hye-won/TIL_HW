# 문자열 뒤집기
s = 'Reverse'
s_lst = list(s)
N = len(s)

for i in range(N//2):
    s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]
print(s_lst)


print(s)
result = ''.join(s_lst)
print(result)
print(''.join(s_lst))


## 문자열 비교
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1, s2, s5)   # abc abc abc

if s1 == s5:  # 내용물 비교하려면 얘로 해야한다.
    print('s1==s5')
else:
    print('s1!=s5')
    '''
s1==s5
'''

if s1 is s5:
    print('s1 is s5')
else:
    print('s1 is not s5')
'''
    s1 is not s5
'''

a = [1,2,3]
a = list(map(str, a))  # ['1', '2', '3']
# a = ''.join(list(map(str, a)))  # 123
print(a)

str()
# 함수를 사용하지않고, itoa()를구현해봅시다.
def itoa(a):
    s= ''
    while a > 0:
        s += chr(ord('0') + a % 10) # 일의 자리 숫자의 코드를 찾아냄(1의 자리 숫자의 ASCII값)
        a //= 10
    return s[::-1]

a = 123
print(a)