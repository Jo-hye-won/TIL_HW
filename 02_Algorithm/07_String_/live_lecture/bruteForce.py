P = 찾을 패턴
T = 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def bruteforce(p,t):
    i = 0   # 찾을 패턴의 인덱스
    j = 0   # 전체 텍스트의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M:  # 전체 텍스트의 인덱스가 전체 패턴의 길이와 같으면
        return i - M   # 패턴의 인덱스에서 패턴의 길이를 빼준다
    else:
        return -1  # 그 외에는 -1 반환
