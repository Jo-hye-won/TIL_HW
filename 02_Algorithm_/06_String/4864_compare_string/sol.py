import sys
sys.stdin = open('input.txt.py')

# 고지식한 패턴검색 함수 정의
def BruteForce(p,t):
    p_idx = 0   # 패턴의 인덱스
    t_idx = 0   # 탐색할 텍스트의 인덱스

    # 패턴의 인덱스 패턴의 길이보다 작고,
    # 탐색할 텍스트의 인덱스 탐색할 텍스트의 길이보다 작은 동안
    while p_idx < len(p) and t_idx < len(t):
        # 탐색할 인덱스 0 위치의 텍스트가
        # 패턴의 인덱스 0 위치의 텍스트와 다르면
        if t[t_idx] != p[p_idx]:
            # 탐색인덱스는 탐색인덱스에서 패턴인덱스 빼주고
            t_idx = t_idx - p_idx  # 그러면 탐색인덱스는 0 - 0을 해서 0이되고
            p_idx = -1  # 패턴 인덱스는 1을 빼줘서 -1이 되고

        # if문 끝나면서 아직 while문 돌아야해서 두 인덱스 모두에 +1 해주면서
        # 다음 탐색을 위한 준비하기
        t_idx = t_idx + 1
        p_idx = p_idx + 1

    # 패턴의 인덱스가 패턴의 길이와 같아져서 같은 글자를 찾았다!!!
    if p_idx == len(p):
        return 1    # 그 때 도출하고싶은 값
    else:
        return 0    # 못찾았을 경우


T = int(input())
for tc in range(1, T+1):
    N = input()     # str1(패턴)
    M = input()     # str2(탐색할텍스트)
    print(f'#{tc} {BruteForce(N,M)}')




#     while 0 < len(M) and 0 < len(N):
# #         if M[i]
# #     # if M in N:
# #     #     cnt += 1
# #     # 이거 쓰지 말고 해봐