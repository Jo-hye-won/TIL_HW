# 재귀 함수
'''
key가 있으면 1, 없으면 0을 리턴하는 함수
'''
def f(i, N, key, arr):  # i = 현재 상태, N = 목표, key = 찾고자 하는 원소
    if i == N:
        return 0    # key가 없는 경우
    elif arr[i] == key:
        return 1
    else:
        return f(i + 1, N, key, arr)


N = 5
A = [1, 2, 3, 4, 5]
key = 3
key2 = 10

print(f(0, N, key, A))
print(f(0, N, key2, A))