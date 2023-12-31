import sys
sys.stdin = open('input.txt', encoding='utf-8')  # 한글을 입력해도 잘 읽어오도록함

# char은 타겟의 값이 내 패턴 안에 몇번째에 있는지 조사
def search(pattern,char):
    # 어디까지 동일한 값을 가지고 있는 지 확인
    for i in range(len(pattern)-2, -1, -1):
        # 동일한 값이 있다면
        if pattern[i] == char:
            # 그 위치까지 이동하도록 index번호 넘겨주기
            return len(pattern) - i - 1

        # char랑 pattern이랑 일치하지 않으면
        return len(pattern)

def boyer_moore(pattern, targatet):
    # 최종 결과값
    result = 0
    # 조사범위
    t_idx = 0
    # 조사 범위를 조금 수정
    while t_idx <= len(target) - len(pattern):
        # 뒤에서부터 조사
        p_idx = len(pattern)
        # P_idx가 0이 되기 전까지
        while p_idx >= 0:
            # 서로 다르다면
            if pattern[p_idx] != target[t_idx + p_idx]:
                #다음 조사위치로 이동하기 위한 값 만들어야 한다.
                next = search(pattern, target[t_idx + len(pattern) -1])
                break
            p_idx -= 1
        if p_idx == -1:
            count += 1
            t_idx += 1
        else:
            t_idx += next
    return result



for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    print(boyer_moore())