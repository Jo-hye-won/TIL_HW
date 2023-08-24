import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    dan = []
    for i in range(N):
        for j in range(i + 1, N):
            dan.append(lst[i] * lst[j])

    dan = list(map(str, dan))

    res = []
    for i in dan:
        if len(i) < 2:
            continue

        check = True    # 단조 증가하는지 체크
        for j in range(len(i) - 1):
            if i[j] > i[j + 1]:  # 앞의 자리가 뒤 자리 보다 크게 되면
                check = False  # check 변환 그러면서
                break          # 바로위 for문 탈출
        if check:              # 방금 포문 아무 이상없이 한바꾸 돌았네 ?
            res.append(int(i))  # 그럼 dan 리스트에 i이놈 정수로 바까서 res에 넣어줘

    if len(res) == 0:
        print(f"#{tc} -1")
    else:
        MAX = max(res)
        print(f"#{tc} {MAX}")