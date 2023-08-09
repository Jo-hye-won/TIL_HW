def solution(word):
    length = len(word)
    check = 0
    answer = 0

    for k in range(length // 2):
        if word[k] == word[length - 1 - k]:
            check += 1

    if check == (length // 2):
        answer += 1

    return answer


T = 10
for t in range(1, T + 1):
    N = 8
    M = int(input())
    str_ls = [list(map(str, input().rstrip())) for _ in range(N)]
    cnt = 0

    for i in range(N):  # 가로, 세로 줄 탐색
        for j in range(N - M + 1):
            word_w = []
            word_h = []
            for wh in range(j, j + M):
                word_w.append(str_ls[i][wh])
                word_h.append(str_ls[wh][i])

            cnt += solution(word_w)
            cnt += solution(word_h)

    print(f'#{t}', cnt)