def solution(word):
    length = len(word)
    check = 0
    answer = 0

    # 길이의 절반만큼잘라서 조사진행하면 된다(회문이라 대칭이라서)
    for k in range(length // 2):
        if word[k] == word[length - 1 - k]:  # 첫글자와 마지막글자 비교해서 같으면(다음은 두번째랑 마지막 앞에 글자겠지)
            check += 1  # 글자수 +1

    if check == (length // 2):  # 세어 둔 글자수가 단어길이의 절반이라면 대칭이라는 거니까
        answer += 1 # 회문 찾았으니까 찾은 회문수  + 1 하기

    return answer  # 회문수 반환하기


T = 10
for t in range(1, T + 1):
    N = 8  # 글자판 8 X 8
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