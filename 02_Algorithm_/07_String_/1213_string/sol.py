# 이번 주 목표로 해라
import sys
sys.stdin = open('input.txt', encoding='utf-8')  # 한글을 입력해도 잘 읽어오도록함

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    # 조사 대상 두개 (PATTERN, TARGET)의 인덱스를 담을 변수 선언
    p_idx = 0
    t_idx = 0

    # 최종 결괏값
    result = 0  # 패턴이 문장에 몇번 들어가는지 센다.

    # 조사를 할건데 언제까지 반복할 것이냐?
    # 타겟의 끝까지 조사하면서, 패턴이 몇 번 나오는지 세야한다.
    len_target = len(target)
    while t_idx < len_target:
        # 두 값이 같다면
        # if target[t_idx] == pattern[p_idx]:
        #     p_idx += 1
        #     t_idx += 1
        # else:
        #     if p_idx != 0:
        #
        #     p_idx = 0  # 패턴 인덱스 다시 처음으로 돌려보냄


        # t_idx번째의 값과 p_idx번째의 값이
        # 같거나 틀릴 때 취해야 할 행동
        if target[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
        # 같거나 틀린 상황 이외에
        # 모든 상황에 대해서
        # p_idx와 t_idx는 증가 할 것
        p_idx += 1
        t_idx += 1

        if p_idx == len(pattern):
            result += 1  # 패턴 한 번 찾았어요
            p_idx = 0  # 다음부터는 다시 0번부터 조사.

    print(f'#{tc} {result}')
