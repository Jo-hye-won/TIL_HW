import sys
sys.stdin = open('input.txt', encoding='utf-8')  # 한글을 입력해도 잘 읽어오도록함

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    # 최종 결괏값
    result = 0
    p_idx = 0
    for t_idx in range(len(target) - len(pattern) + 1):
        if p_idx and t_idx + p_idx <= last_t_idx + len(pattern):
            continue

        for p_idx in range(len(pattern)):
            # 패턴과 타겟이 동일하지 않은 경우가 한번이라도 나오면 조사 종료
            if pattern[p_idx] != target[t_idx+p_idx]:
                last_t_idx = t_idx
                p_idx = 0
                break
    else:  # for문도 else가 있다 : break 된 적 없이 모두 순회했을때,
        result += 1
        last_t_idx = t_idx

    print(result)