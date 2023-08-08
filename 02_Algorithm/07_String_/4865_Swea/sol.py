import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):    # 테스트 케이스 만큼 돌면서
    P = input()             # 찾을 패턴
    # ran = list(P)
    Find = input()          # 패턴 찾을 값

    max_find = 0            # 가장 큰 값 초기화
    # for p in ran:
    for p in P:             # 찾을 패턴에서 비교할 값을 하나씩 들고와서
        f_idx = 0           # 패턴찾을값의 인덱스 번호
        result = 0          # 비교할 값이 몇개인지 세기위한 초기값 설정
        len_target = len(Find)  # 패턴을 찾을 값의 길이만큼 돌아야함
        while f_idx < len_target:
            if p == Find[f_idx]:    # 패턴에서 꺼내온 값이랑 Find의 값이 같으면
                result += 1         # 결과값 +1
            f_idx += 1              # 인덱스는 계속 1씩 증가
        if max_find < result:       # 결과값이 가장큰값보다 크면
            max_find = result       # 가장큰값을 결과값으로 갱신

    print(f'#{tc} {max_find}')





        # if p_idx == len(pattern):
        #     result += 1  # 패턴 한 번 찾았어요
        #     p_idx = 0  # 다음부터는 다시 0번부터 조사.


